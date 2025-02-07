"""Common utility functions for the application"""
from typing import Set, Dict, Any, List, Optional
import json
from datetime import datetime
from config.database import get_db
from sqlalchemy.orm import Session

def get_effective_memberships(username: str) -> Set[str]:
    """
    Get all effective group memberships for a user including nested groups
    
    Args:
        username: The username to get memberships for
        
    Returns:
        Set of group names the user is effectively a member of
    """
    try:
        effective_groups = set()
        with get_db() as db:
            cursor = db.cursor()
            
            # Get all groups
            cursor.execute("SELECT name, members FROM groups")
            all_groups = cursor.fetchall()
            
            # Build group membership map
            group_map = {}
            for group in all_groups:
                group_map[group['name']] = json.loads(group['members'])
            
            def resolve_user_groups(username: str, visited: Set[str] = None) -> None:
                if visited is None:
                    visited = set()
                    
                # Check each group
                for group_name, members in group_map.items():
                    if group_name in visited:
                        continue
                        
                    visited.add(group_name)
                    
                    # If user is a direct member
                    if username in members:
                        effective_groups.add(group_name)
                        # Check for parent groups that contain this group
                        for parent_name, parent_members in group_map.items():
                            if f"group_{group_name}" in parent_members:
                                resolve_user_groups(f"group_{group_name}", visited)
            
            resolve_user_groups(username)
            return effective_groups
            
    except Exception as e:
        print(f"Error resolving effective memberships for user {username}: {e}")
        return set()

def get_nested_members(group_name: str) -> Set[str]:
    """
    Get all members of a group including those from nested groups
    
    Args:
        group_name: Name of the group to get members for
        
    Returns:
        Set of all member usernames, including those from nested groups
    """
    try:
        visited_groups = set()
        all_members = set()
        
        def resolve_group(group_name: str) -> None:
            """Recursively resolve group members"""
            if group_name in visited_groups:
                return
            
            visited_groups.add(group_name)
            
            with get_db() as db:
                cursor = db.cursor()
                cursor.execute("SELECT members FROM groups WHERE name = ?", (group_name,))
                group = cursor.fetchone()
                
                if group and group['members']:
                    members = json.loads(group['members'])
                    for member in members:
                        if member.startswith('group_'):
                            # It's a nested group, resolve it
                            nested_group = member.replace('group_', '', 1)
                            resolve_group(nested_group)
                        else:
                            # It's a user
                            all_members.add(member)
        
        resolve_group(group_name)
        return all_members
        
    except Exception as e:
        print(f"Error resolving nested members for group {group_name}: {e}")
        return set()

def track_relationship_changes(
    entity_type: str,
    entity_id: int,
    old_state: Dict[str, Any],
    new_state: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Track changes in relationships between entities
    
    Args:
        entity_type: Type of entity being changed ('user' or 'group')
        entity_id: ID of the entity being changed
        old_state: Previous state of the entity
        new_state: New state of the entity
        
    Returns:
        Dict containing affected entities and required version updates
    """
    changes = {
        'entity_type': entity_type,
        'entity_id': entity_id,
        'timestamp': datetime.utcnow().isoformat(),
        'cascaded_versions': []
    }
    
    # Track membership changes
    old_memberships = set(json.loads(old_state['memberships']) if isinstance(old_state['memberships'], str) 
                         else old_state['memberships'])
    new_memberships = set(json.loads(new_state['memberships']) if isinstance(new_state['memberships'], str) 
                         else new_state['memberships'])
    
    # Record affected groups
    affected_groups = old_memberships.union(new_memberships)
    for group_name in affected_groups:
        changes['cascaded_versions'].append({
            'type': 'group',
            'id': group_name,
            'action': 'version'
        })
    
    return changes

def log_version_change(
    old_state: Dict[str, Any],
    new_state: Dict[str, Any],
    changes: Dict[str, Any]
) -> None:
    """
    Log version changes for audit purposes
    
    Args:
        old_state: Previous entity state
        new_state: New entity state
        changes: Dictionary of tracked changes
    """
    # TODO: Implement proper logging
    pass

def log_group_version_change(
    old_state: Dict[str, Any],
    new_state: Dict[str, Any],
    changes: Dict[str, Any]
) -> None:
    """
    Log group version changes for audit purposes
    
    Args:
        old_state: Previous group state
        new_state: New group state
        changes: Dictionary of tracked changes
    """
    # TODO: Implement proper logging
    pass

def get_active_history_record(records: List[Any]) -> Optional[Any]:
    """Get the currently active history record"""
    now = datetime.utcnow()
    return next(
        (r for r in records if r.start_date <= now and (not r.end_date or r.end_date > now)),
        None
    )

def create_history_record(
    db: Session,
    model_class: Any,
    entity_id: int,
    data: Dict[str, Any],
    start_date: datetime = None
) -> Any:
    """Create a new history record"""
    if not start_date:
        start_date = datetime.utcnow()
        
    # Close any active history records
    active_record = get_active_history_record(
        db.query(model_class)
        .filter_by(**{f"{model_class.__tablename__.split('_')[0]}_id": entity_id})
        .all()
    )
    if active_record:
        active_record.end_date = start_date
        
    # Create new history record
    new_record = model_class(
        **data,
        start_date=start_date,
        end_date=None
    )
    db.add(new_record)
    return new_record

def get_nested_group_members(db: Session, group_id: int, visited: Set[int] = None) -> Set[str]:
    """Get all nested group members"""
    if visited is None:
        visited = set()
    
    if group_id in visited:
        return set()
    
    visited.add(group_id)
    members = set()
    
    group = db.query(GroupDB).get(group_id)
    if not group:
        return members
    
    # Add direct members
    for membership in group.memberships:
        members.add(membership.user.user_name)
    
    # Add nested members
    for membership in group.memberships:
        members.update(get_nested_group_members(db, membership.group_id, visited))
    
    return members

def validate_membership_cycle(db: Session, group_id: int, member_group_id: int) -> bool:
    """Check for membership cycles when adding groups"""
    visited = set()
    
    def check_cycle(current_id: int) -> bool:
        if current_id in visited:
            return True
        if current_id == group_id:
            return True
            
        visited.add(current_id)
        group = db.query(GroupDB).get(current_id)
        if not group:
            return False
            
        for membership in group.memberships:
            if check_cycle(membership.group_id):
                return True
                
        visited.remove(current_id)
        return False
    
    return check_cycle(member_group_id) 