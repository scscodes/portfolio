"""Database models for membership domain"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from config.database import Base

class Membership(Base):
    """Membership model"""
    __tablename__ = 'membership'

    membership_id = Column(Integer, primary_key=True)
    membership_name = Column(String, nullable=False)
    
    # Relationships
    user_memberships = relationship("UserMembership", back_populates="membership")
    group_memberships = relationship("GroupMembership", back_populates="membership")
    history = relationship("MembershipHistory", back_populates="membership")

class MembershipHistory(Base):
    """Membership version history"""
    __tablename__ = 'membership_history'

    membership_history_id = Column(Integer, primary_key=True)
    membership_id = Column(Integer, ForeignKey('membership.membership_id'), nullable=False)
    membership_name = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=True)

    # Relationship
    membership = relationship("Membership", back_populates="history")

class UserMembership(Base):
    """User-Membership association"""
    __tablename__ = 'user_membership'

    user_membership_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    membership_id = Column(Integer, ForeignKey('membership.membership_id'), nullable=False)
    
    # Unique constraint for user-membership combination
    __table_args__ = (
        UniqueConstraint('user_id', 'membership_id', name='uix_user_membership'),
    )

    # Relationships
    user = relationship("UserDB", back_populates="memberships")
    membership = relationship("Membership", back_populates="user_memberships")
    history = relationship("UserMembershipHistory", back_populates="user_membership")

class GroupMembership(Base):
    """Group-Membership association"""
    __tablename__ = 'group_membership'

    group_membership_id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('group.group_id'), nullable=False)
    membership_id = Column(Integer, ForeignKey('membership.membership_id'), nullable=False)
    
    # Unique constraint for group-membership combination
    __table_args__ = (
        UniqueConstraint('group_id', 'membership_id', name='uix_group_membership'),
    )

    # Relationships
    group = relationship("GroupDB", back_populates="memberships")
    membership = relationship("Membership", back_populates="group_memberships")
    history = relationship(
        "GroupMembershipHistory",
        back_populates="group_membership",
        primaryjoin="and_(GroupMembership.group_membership_id==GroupMembershipHistory.group_membership_id)"
    )

class UserMembershipHistory(Base):
    """User-Membership association history"""
    __tablename__ = 'user_membership_history'

    user_membership_history_id = Column(Integer, primary_key=True)
    user_membership_id = Column(Integer, ForeignKey('user_membership.user_membership_id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    membership_id = Column(Integer, ForeignKey('membership.membership_id'), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=True)

    # Relationships
    user = relationship("UserDB", back_populates="membership_history")
    user_membership = relationship("UserMembership", back_populates="history")

class GroupMembershipHistory(Base):
    """Group-Membership association history"""
    __tablename__ = 'group_membership_history'

    group_membership_history_id = Column(Integer, primary_key=True)
    group_membership_id = Column(Integer, ForeignKey('group_membership.group_membership_id'), nullable=False)
    group_id = Column(Integer, ForeignKey('group.group_id'), nullable=False)
    membership_id = Column(Integer, ForeignKey('membership.membership_id'), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=True)

    # Relationships
    group = relationship("GroupDB", back_populates="membership_history")
    group_membership = relationship("GroupMembership", back_populates="history") 