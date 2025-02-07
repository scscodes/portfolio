"""
Report Schema Analysis

1. Input Schemas (Used for API requests)
-----------------------------------------
ReportRequest:
    - Used in: POST /reports
    - Purpose: Define parameters for generating a new report
    Example:
    {
        "report_type": "full",
        "target_id": null,
        "properties": {"include_historical": true}
    }

2. Base Response Schemas
-----------------------------------------
ReportBase:
    - Base schema with common report fields
    - Extended by other response schemas

ReportResponse:
    - Used in: GET /reports, POST /reports
    - Basic report metadata without snapshots
    Example:
    {
        "id": 1,
        "report_type": "full",
        "status": "completed",
        "created_at": "2024-02-06T..."
    }

3. Snapshot Schemas (Used in detailed responses)
-----------------------------------------
GroupSnapshotResponse:
    - Used in: GET /reports/{id}/groups
    - Point-in-time view of a group
    Example:
    {
        "group_name": "IT_Department",
        "direct_members": ["user1", "user2"],
        "nested_members": ["user3"]
    }

UserSnapshotResponse:
    - Used in: GET /reports/{id}/users
    - Point-in-time view of a user
    Example:
    {
        "username": "john_doe",
        "direct_memberships": ["IT", "Developers"]
    }

4. Detailed Report Schemas
-----------------------------------------
DetailedReportResponse:
    - Used in: GET /reports/{id}
    - Complete report with all snapshots
    - Extends ReportResponse
    Example:
    {
        ...report metadata...,
        "group_snapshots": [...],
        "user_snapshots": [...]
    }

5. Historical Schemas (Can be deprecated)
-----------------------------------------
MembershipReport, UserMembershipHistory, GroupMembershipHistory:
    - These appear to be older schemas
    - Can be removed as they're replaced by the snapshot system
"""

# Suggested cleanup:
from datetime import datetime
from typing import Dict, Any, Optional, List, Literal
from pydantic import BaseModel

# 1. Input Schema
class ReportRequest(BaseModel):
    """
    Input schema for report generation requests
    Used in: POST /reports
    
    Example:
    {
        "report_type": "full",
        "target_id": null,
        "properties": {
            "include_historical": true,
            "depth": "all"
        }
    }
    """
    report_type: Literal["full", "group_specific", "user_specific", "membership_specific"]
    target_id: Optional[str] = None
    properties: Dict[str, Any] = {}

# 2. Base Response Schemas
class ReportBase(BaseModel):
    """
    Base schema for all report responses
    Contains common fields used across different report types
    Extended by: ReportResponse, DetailedReportResponse
    
    Example:
    {
        "report_type": "full",
        "status": "completed",
        "created_at": "2024-02-06T12:00:00Z",
        "completed_at": "2024-02-06T12:01:00Z",
        "properties": {...}
    }
    """
    report_type: str
    target_id: Optional[str]
    status: str
    properties: Dict[str, Any]
    created_at: datetime
    completed_at: Optional[datetime]

    class Config:
        from_attributes = True

class ReportResponse(ReportBase):
    """
    Basic report response schema
    Used in: GET /reports (list endpoint)
    Adds: report ID to base fields
    
    Example:
    {
        "id": 1,
        ...base fields...
    }
    """
    id: int

# 3. Snapshot Schemas
class SnapshotBase(BaseModel):
    """
    Base schema for point-in-time snapshots
    Extended by: GroupSnapshotResponse, UserSnapshotResponse
    Contains: Common snapshot metadata
    """
    snapshot_time: datetime
    properties: Dict[str, Any]

    class Config:
        from_attributes = True

class GroupSnapshotResponse(SnapshotBase):
    """
    Group snapshot schema
    Used in: GET /reports/{id}/groups
    Purpose: Captures group state at a specific point in time
    
    Example:
    {
        "group_name": "IT_Department",
        "direct_members": ["user1", "user2"],
        "nested_members": ["user3", "user4"],
        "member_of": ["Organization"],
        "all_parent_groups": ["Organization", "IT"],
        "snapshot_time": "2024-02-06T12:00:00Z",
        "properties": {
            "type": "department",
            "cost_center": "IT001"
        }
    }
    """
    group_name: str
    description: Optional[str]
    direct_members: List[str]
    nested_members: List[str]
    member_of: List[str]
    all_parent_groups: List[str]

class UserSnapshotResponse(SnapshotBase):
    """
    User snapshot schema
    Used in: GET /reports/{id}/users
    Purpose: Captures user membership state at a specific point in time
    
    Example:
    {
        "username": "john_doe",
        "email": "john@company.com",
        "full_name": "John Doe",
        "direct_memberships": ["IT", "Developers"],
        "effective_memberships": ["IT", "Developers", "Organization"],
        "snapshot_time": "2024-02-06T12:00:00Z",
        "properties": {
            "title": "Senior Developer",
            "access_level": "high"
        }
    }
    """
    username: str
    email: str
    full_name: str
    direct_memberships: List[str]
    effective_memberships: List[str]

# 4. Detailed Report Schema
class DetailedReportResponse(ReportResponse):
    """
    Complete report response with all snapshots
    Used in: GET /reports/{id}
    Extends: ReportResponse
    Adds: Group and user snapshots
    
    Example:
    {
        "id": 1,
        "report_type": "full",
        ...base fields...,
        "group_snapshots": [
            {group snapshot objects...}
        ],
        "user_snapshots": [
            {user snapshot objects...}
        ]
    }
    """
    group_snapshots: List[GroupSnapshotResponse]
    user_snapshots: List[UserSnapshotResponse] 