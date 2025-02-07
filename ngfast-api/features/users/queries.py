"""Database queries for user domain"""
from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import List, Optional

from .models import UserDB, UserVersion
from .schemas import UserCreate, UserUpdate

class UserQueries:
    def __init__(self, db: Session):
        self.db = db

    def get_all_users(self) -> List[UserDB]:
        """Get all users"""
        return self.db.query(UserDB).all()

    def get_user_by_id(self, user_id: int) -> Optional[UserDB]:
        """Get user by ID"""
        return self.db.query(UserDB).filter(UserDB.user_id == user_id).first()

    def create_user(self, user_data: UserCreate) -> UserDB:
        """Create a new user"""
        db_user = UserDB(
            user_name=user_data.user_name,
            email=user_data.email,
            full_name=user_data.full_name,
            principal_name=user_data.principal_name,
            properties=user_data.properties
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update_user(self, user_id: int, user_data: UserUpdate) -> Optional[UserDB]:
        """Update user details"""
        user = self.get_user_by_id(user_id)
        if not user:
            return None

        update_data = user_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(user, key, value)

        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_history(self, user_id: int) -> List[UserVersion]:
        """Get version history for a user"""
        return self.db.query(UserVersion)\
            .filter(UserVersion.user_id == user_id)\
            .order_by(UserVersion.version.desc())\
            .all()

    def get_user_version(self, user_id: int, version_id: int) -> Optional[UserVersion]:
        """Get specific version of a user"""
        return self.db.query(UserVersion)\
            .filter(
                UserVersion.user_id == user_id,
                UserVersion.id == version_id
            ).first()

INSERT_USER = """
INSERT INTO users (
    username, email, full_name, memberships,
    properties, created_at, modified_at, evaluated_at
) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

INSERT_USER_VERSION = """
INSERT INTO user_versions (
    user_id, username, email, full_name,
    memberships, properties, created_at,
    modified_at, evaluated_at, archived_at
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""