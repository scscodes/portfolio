"""Membership service layer"""
from datetime import datetime
from typing import Optional, List
from sqlalchemy.orm import Session
from fastapi import HTTPException

from .models import (
    Membership, MembershipHistory,
    UserMembership, UserMembershipHistory,
    GroupMembership, GroupMembershipHistory
)
from shared.utils import create_history_record
from shared.exceptions import InvalidMembershipError

class MembershipService:
    def __init__(self, db: Session):
        self.db = db

    def add_user_to_membership(
        self,
        user_id: int,
        membership_id: int,
        start_date: datetime = None
    ) -> UserMembership:
        """Add user to membership with history tracking"""
        try:
            if not start_date:
                start_date = datetime.utcnow()

            user_membership = UserMembership(
                user_id=user_id,
                membership_id=membership_id
            )
            self.db.add(user_membership)
            self.db.flush()

            history = create_history_record(
                self.db,
                UserMembershipHistory,
                user_membership.user_id,
                {
                    "user_id": user_id,
                    "membership_id": membership_id,
                    "user_membership_id": user_membership.user_membership_id
                },
                start_date
            )
            
            self.db.commit()
            return user_membership
        except Exception as e:
            self.db.rollback()
            raise InvalidMembershipError(str(e))

    def remove_user_from_membership(
        self,
        user_id: int,
        membership_id: int,
        end_date: datetime = None
    ) -> None:
        """Remove user from membership with history tracking"""
        if not end_date:
            end_date = datetime.utcnow()

        # Update history record
        active_record = self.db.query(UserMembershipHistory)\
            .filter_by(user_id=user_id, membership_id=membership_id)\
            .filter_by(end_date=None)\
            .first()

        if active_record:
            active_record.end_date = end_date
            self.db.commit()

    def get_user_memberships(
        self,
        user_id: int,
        include_historical: bool = False
    ) -> List[UserMembershipResponse]:
        """Get user memberships"""
        query = self.db.query(UserMembershipHistory)\
            .filter_by(user_id=user_id)
        
        if not include_historical:
            query = query.filter(
                (UserMembershipHistory.end_date.is_(None)) |
                (UserMembershipHistory.end_date > datetime.utcnow())
            )
        
        return query.order_by(UserMembershipHistory.start_date.desc()).all()

    def get_group_memberships(
        self,
        group_id: int,
        include_historical: bool = False
    ) -> List[GroupMembershipResponse]:
        """Get group memberships"""
        query = self.db.query(GroupMembershipHistory)\
            .filter_by(group_id=group_id)
        
        if not include_historical:
            query = query.filter(
                (GroupMembershipHistory.end_date.is_(None)) |
                (GroupMembershipHistory.end_date > datetime.utcnow())
            )
        
        return query.order_by(GroupMembershipHistory.start_date.desc()).all() 