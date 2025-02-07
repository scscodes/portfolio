"""User service layer"""
from datetime import datetime
from typing import Optional, List, Dict
from sqlalchemy.orm import Session
from fastapi import HTTPException

from .models import UserDB, UserHistory
from features.memberships.models import UserMembershipHistory
from .schemas import UserCreate, UserUpdate
from shared.utils import create_history_record
from shared.exceptions import EntityNotFoundError

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_data: UserCreate) -> UserDB:
        """Create a new user with history"""
        # Create user
        user = UserDB(
            user_name=user_data.user_name,
            email=user_data.email,
            full_name=user_data.full_name,
            principal_name=user_data.principal_name,
            properties=user_data.properties
        )
        self.db.add(user)
        self.db.flush()

        # Create initial history record
        create_history_record(
            self.db,
            UserHistory,
            user.user_id,
            {
                "user_id": user.user_id,
                "user_name": user.user_name
            }
        )
        
        self.db.commit()
        return user

    def update_user(self, user_id: int, user_data: UserUpdate) -> UserDB:
        """Update user with history tracking"""
        user = self.db.query(UserDB).filter_by(user_id=user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        # Update user fields
        update_data = user_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(user, key, value)

        # Create history record if user_name changed
        if 'user_name' in update_data:
            create_history_record(
                self.db,
                UserHistory,
                user.user_id,
                {
                    "user_id": user.user_id,
                    "user_name": user.user_name
                }
            )

        self.db.commit()
        return user

    def get_all_users(self) -> List[UserDB]:
        """Get all users"""
        return self.db.query(UserDB).all()

    def get_user_by_id(self, user_id: int) -> Optional[UserDB]:
        """Get user by ID"""
        return self.db.query(UserDB).filter_by(user_id=user_id).first()

    def get_user_history(self, user_id: int) -> List[UserHistory]:
        """Get user history"""
        return self.db.query(UserHistory)\
            .filter_by(user_id=user_id)\
            .order_by(UserHistory.start_date.desc())\
            .all()

    def get_membership_history(self, user_id: int) -> List[Dict]:
        """Get user's membership history"""
        user = self.get_user_by_id(user_id)
        if not user:
            raise EntityNotFoundError("User", user_id)
        
        return self.db.query(UserMembershipHistory)\
            .filter_by(user_id=user_id)\
            .order_by(UserMembershipHistory.start_date.desc())\
            .all() 