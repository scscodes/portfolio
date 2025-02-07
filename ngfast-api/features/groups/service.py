"""Group service layer"""
from datetime import datetime
from typing import Optional, List, Dict
from sqlalchemy.orm import Session
from fastapi import HTTPException

from .models import GroupDB, GroupHistory
from features.memberships.models import GroupMembershipHistory  # Import from memberships
from .schemas import (
    GroupCreate, 
    GroupUpdate,
    GroupMemberships
)
from shared.utils import create_history_record
from shared.exceptions import EntityNotFoundError

class GroupService:
    def __init__(self, db: Session):
        self.db = db

    def create_group(self, group_data: GroupCreate) -> GroupDB:
        """Create a new group with history"""
        group = GroupDB(
            group_name=group_data.group_name,
            description=group_data.description,
            properties=group_data.properties
        )
        self.db.add(group)
        self.db.flush()

        create_history_record(
            self.db,
            GroupHistory,
            group.group_id,
            {
                "group_id": group.group_id,
                "group_name": group.group_name
            }
        )
        
        self.db.commit()
        return group

    def update_group(self, group_id: int, group_data: GroupUpdate) -> GroupDB:
        """Update group with history tracking"""
        group = self.db.query(GroupDB).filter_by(group_id=group_id).first()
        if not group:
            raise HTTPException(status_code=404, detail="Group not found")

        update_data = group_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(group, key, value)

        if 'group_name' in update_data:
            create_history_record(
                self.db,
                GroupHistory,
                group.group_id,
                {
                    "group_id": group.group_id,
                    "group_name": group.group_name
                }
            )

        self.db.commit()
        return group

    def get_all_groups(self) -> List[GroupDB]:
        """Get all groups"""
        return self.db.query(GroupDB).all()

    def get_group_by_id(self, group_id: int) -> Optional[GroupDB]:
        """Get group by ID"""
        return self.db.query(GroupDB).filter_by(group_id=group_id).first()

    def get_group_history(self, group_id: int) -> List[GroupHistory]:
        """Get group history"""
        return self.db.query(GroupHistory)\
            .filter_by(group_id=group_id)\
            .order_by(GroupHistory.start_date.desc())\
            .all()

    def get_group_members(self, group_id: int) -> GroupMemberships:
        """
        Get group members through membership associations
        
        The relationship chain is:
        Group -> GroupMembership -> Membership -> UserMembership -> User
        """
        group = self.get_group_by_id(group_id)
        if not group:
            raise EntityNotFoundError("Group", group_id)
        
        # Get direct members through memberships
        direct_members = []
        for group_membership in group.memberships:
            # Get the membership object
            membership = group_membership.membership
            # Get all user memberships for this membership
            for user_membership in membership.user_memberships:
                if not user_membership.end_date:  # Only active memberships
                    direct_members.append(user_membership.user.user_name)
        
        # TODO: Implement nested membership resolution
        nested_members = []
        
        return GroupMemberships(
            direct=direct_members,
            nested=nested_members
        )

    def get_membership_history(self, group_id: int) -> List[Dict]:
        """Get group's membership history"""
        group = self.get_group_by_id(group_id)
        if not group:
            raise EntityNotFoundError("Group", group_id)
        
        return self.db.query(GroupMembershipHistory)\
            .filter_by(group_id=group_id)\
            .order_by(GroupMembershipHistory.start_date.desc())\
            .all() 