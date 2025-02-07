from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Membership, UserMembership, GroupMembership

class MembershipQueries:
    """
    Queries for managing memberships and their relationships
    """
    def __init__(self, db: Session):
        self.db = db

    def get_user_memberships(self, user_id: int, include_historical: bool = False):
        """
        Get all memberships for a user
        """
        query = select(UserMembership).where(UserMembership.user_id == user_id)
        if not include_historical:
            query = query.where(
                (UserMembership.end_date.is_(None)) | 
                (UserMembership.end_date > datetime.utcnow())
            )
        return self.db.execute(query).scalars().all()

    def get_group_memberships(self, group_id: int, include_historical: bool = False):
        """
        Get all memberships for a group
        """
        query = select(GroupMembership).where(GroupMembership.group_id == group_id)
        if not include_historical:
            query = query.where(
                (GroupMembership.end_date.is_(None)) | 
                (GroupMembership.end_date > datetime.utcnow())
            )
        return self.db.execute(query).scalars().all()

    def get_membership_users(self, membership_id: int, active_only: bool = True):
        """
        Get all users with a specific membership
        """
        query = select(UserMembership).where(
            UserMembership.membership_id == membership_id
        )
        if active_only:
            query = query.where(
                (UserMembership.end_date.is_(None)) | 
                (UserMembership.end_date > datetime.utcnow())
            )
        return self.db.execute(query).scalars().all() 