"""Database models for report domain"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class MembershipReport(Base):
    """Report model"""
    __tablename__ = 'membership_reports'

    id = Column(Integer, primary_key=True)
    report_type = Column(String, nullable=False)
    target_id = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False)
    completed_at = Column(DateTime, nullable=True)
    status = Column(String, nullable=False)
    properties = Column(JSON, nullable=False, default={})

    # Relationships
    group_snapshots = relationship("GroupSnapshot", back_populates="report")
    user_snapshots = relationship("UserSnapshot", back_populates="report")

class GroupSnapshot(Base):
    """Group snapshot model"""
    __tablename__ = 'group_snapshots'

    id = Column(Integer, primary_key=True)
    report_id = Column(Integer, ForeignKey('membership_reports.id'), nullable=False)
    group_name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    direct_members = Column(JSON, nullable=False, default=[])
    nested_members = Column(JSON, nullable=False, default=[])
    member_of = Column(JSON, nullable=False, default=[])
    all_parent_groups = Column(JSON, nullable=False, default=[])
    properties = Column(JSON, nullable=False, default={})
    snapshot_time = Column(DateTime, nullable=False)
    original_created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    original_modified_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    # Relationship
    report = relationship("MembershipReport", back_populates="group_snapshots")

class UserSnapshot(Base):
    """User snapshot model"""
    __tablename__ = 'user_snapshots'

    id = Column(Integer, primary_key=True)
    report_id = Column(Integer, ForeignKey('membership_reports.id'), nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    principal_name = Column(String, nullable=False)
    direct_memberships = Column(JSON, nullable=False, default=[])
    effective_memberships = Column(JSON, nullable=False, default=[])
    properties = Column(JSON, nullable=False, default={})
    snapshot_time = Column(DateTime, nullable=False)
    original_created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    original_modified_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    # Relationship
    report = relationship("MembershipReport", back_populates="user_snapshots") 