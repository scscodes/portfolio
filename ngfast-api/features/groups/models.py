"""Database models for group domain"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import BIGINT
from sqlalchemy import Integer  # Added for SQLite compatibility
from config.database import Base

class GroupDB(Base):
    """Group model"""
    __tablename__ = 'group'

    group_id = Column(Integer, primary_key=True)
    group_name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    properties = Column(JSON, nullable=False, default={})
    
    # Relationships
    history = relationship("GroupHistory", back_populates="group")
    memberships = relationship("GroupMembership", back_populates="group")

    @property
    def users(self):
        """Returns all users in the group through memberships"""
        return [
            membership.membership.users 
            for membership in self.memberships 
            if not membership.end_date
        ]

class GroupHistory(Base):
    """Group version history"""
    __tablename__ = 'group_history'

    group_history_id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('group.group_id'), nullable=False)
    group_name = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=True)

    # Relationship
    group = relationship("GroupDB", back_populates="history")
