"""Database models for user domain"""
from datetime import datetime
from typing import Dict, Any, Optional, List
from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import BIGINT

from config.database import Base

# SQLAlchemy Models
class UserDB(Base):
    """User model"""
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    principal_name = Column(String, unique=True, nullable=False)
    properties = Column(JSON, nullable=False, default={})
    
    # Relationships
    history = relationship("UserHistory", back_populates="user")
    memberships = relationship("UserMembership", back_populates="user")

    @property
    def groups(self):
        """Returns all groups the user belongs to through memberships"""
        return [
            membership.membership.groups 
            for membership in self.memberships 
            if not membership.end_date
        ]

class UserHistory(Base):
    """User version history"""
    __tablename__ = 'user_history'

    user_history_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    user_name = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=True)

    # Relationship
    user = relationship("UserDB", back_populates="history")
