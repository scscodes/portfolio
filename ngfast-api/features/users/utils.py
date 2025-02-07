"""User business logic and operations"""
import json
from typing import Any, Dict, List, Optional
from .models import UserCreate, UserResponse


def log_version_change(old_state: Dict[str, Any], new_state: Dict[str, Any], change_type: str = "update"):
    """Log changes between user versions in a structured way"""
    old_memberships = set(json.loads(old_state['memberships']) if isinstance(old_state['memberships'], str) 
                         else old_state['memberships'])
    new_memberships = set(json.loads(new_state['memberships']) if isinstance(new_state['memberships'], str) 
                         else new_state['memberships'])
    
    added = new_memberships - old_memberships
    removed = old_memberships - new_memberships
    
    print(f"\nUser Version Change - {change_type}")
    print(f"User: {old_state['username']}")
    print(f"Timestamp: {datetime.utcnow().isoformat()}")
    if added or removed:
        print("Membership Changes:")
        if added:
            print(f"  Added: {list(added)}")
        if removed:
            print(f"  Removed: {list(removed)}")
    
    # Log other field changes
    changed_fields = []
    for field in ['email', 'full_name', 'properties']:
        if old_state[field] != new_state[field]:
            changed_fields.append(field)
    
    if changed_fields:
        print(f"Updated Fields: {changed_fields}")
    print("-" * 50) 
