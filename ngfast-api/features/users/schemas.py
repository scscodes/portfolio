"""Pydantic schemas for user domain models and API responses"""
from datetime import datetime
from typing import Dict, Any, Optional, List
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    """Base schema defining core user attributes used for both creation and responses"""
    user_name: str
    email: EmailStr
    full_name: str
    principal_name: str
    properties: Dict[str, Any] = {}

class UserCreate(UserBase):
    """Request schema for user creation endpoint"""
    pass

class UserUpdate(BaseModel):
    """Request schema for PATCH /users/{user_id} endpoint
    All fields are optional to support partial updates"""
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    principal_name: Optional[str] = None
    properties: Optional[Dict[str, Any]] = None

class UserHistory(BaseModel):
    """Response schema for /users/{user_id}/history endpoint
    Represents a historical version of a user"""
    user_history_id: int
    user_id: int
    user_name: str
    start_date: datetime
    end_date: Optional[datetime]

    class Config:
        from_attributes = True

class User(UserBase):
    """Response schema for user endpoints including GET /users and GET /users/{user_id}"""
    user_id: int

    class Config:
        from_attributes = True

class UserMemberships(BaseModel):
    """Response schema for GET /users/{user_id}/memberships endpoint
    Includes both direct and effective memberships through group hierarchies"""
    direct: List[str]
    effective: List[str]

    class Config:
        from_attributes = True

# Schemas that appear unused and can be deprecated:

class UserMembershipHistory(BaseModel):
    """DEPRECATED: Consider removing or implementing in membership history feature"""
    user_id: int
    membership_id: int
    start_date: datetime
    end_date: Optional[datetime]
    membership_name: str
    properties: Dict[str, Any]

    class Config:
        from_attributes = True

class UserMembershipSummary(BaseModel):
    """DEPRECATED: Consider removing or implementing in membership summary feature"""
    direct_memberships: List[str]
    inherited_memberships: List[str]
    historical_memberships: List[UserMembershipHistory]

    class Config:
        from_attributes = True 