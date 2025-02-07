"""Pydantic schemas for group domain models and API responses"""
from datetime import datetime
from typing import Dict, Any, Optional, List
from pydantic import BaseModel

class GroupBase(BaseModel):
    """Base schema defining core group attributes used for both creation and responses"""
    group_name: str
    description: Optional[str] = None
    properties: Dict[str, Any] = {}

class GroupCreate(GroupBase):
    """Request schema for group creation endpoint"""
    pass

class GroupUpdate(BaseModel):
    """Request schema for PATCH /groups/{group_id} endpoint
    All fields are optional to support partial updates"""
    group_name: Optional[str] = None
    description: Optional[str] = None
    properties: Optional[Dict[str, Any]] = None

class GroupHistory(BaseModel):
    """Response schema for /groups/{group_id}/history endpoint
    Represents a historical version of a group"""
    group_history_id: int
    group_id: int
    group_name: str
    start_date: datetime
    end_date: Optional[datetime]

    class Config:
        from_attributes = True

class Group(GroupBase):
    """Response schema for group endpoints including GET /groups and GET /groups/{group_id}"""
    group_id: int

    class Config:
        from_attributes = True

class GroupMemberships(BaseModel):
    """Response schema for GET /groups/{group_id}/members endpoint
    Includes both direct members and nested members through group hierarchies"""
    direct: List[str]
    nested: List[str]

    class Config:
        from_attributes = True

# Schemas that appear unused and can be deprecated:

class GroupMembershipHistory(BaseModel):
    """DEPRECATED: Not currently used in any endpoint
    Consider removing or implementing in membership history feature"""
    group_id: int
    membership_id: int
    start_date: datetime
    end_date: Optional[datetime]
    membership_name: str
    properties: Dict[str, Any]

    class Config:
        from_attributes = True

class GroupMembershipSummary(BaseModel):
    """DEPRECATED: Not currently used in any endpoint
    Consider removing or implementing in membership summary feature"""
    direct_members: List[str]
    nested_members: List[str]
    historical_members: List[GroupMembershipHistory]
    member_of: List[str]

    class Config:
        from_attributes = True 