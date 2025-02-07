"""Pydantic schemas for membership domain"""
from datetime import datetime
from typing import Dict, Any, Optional, List
from pydantic import BaseModel

class MembershipBase(BaseModel):
    """Base membership attributes"""
    membership_name: str

class MembershipCreate(MembershipBase):
    """Schema for membership creation"""
    pass

class MembershipUpdate(MembershipBase):
    """Schema for membership updates"""
    membership_name: Optional[str] = None

class MembershipHistory(BaseModel):
    """Schema for membership history records"""
    membership_history_id: int
    membership_id: int
    membership_name: str
    start_date: datetime
    end_date: Optional[datetime]

    class Config:
        from_attributes = True

class MembershipResponse(MembershipBase):
    """Schema for membership responses"""
    membership_id: int

    class Config:
        from_attributes = True

class UserMembershipResponse(BaseModel):
    """Schema for user membership responses"""
    user_id: int
    membership_id: int
    start_date: datetime
    end_date: Optional[datetime]

    class Config:
        from_attributes = True

class GroupMembershipResponse(BaseModel):
    """Schema for group membership responses"""
    group_id: int
    membership_id: int
    start_date: datetime
    end_date: Optional[datetime]

    class Config:
        from_attributes = True 