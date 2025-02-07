"""Admin domain models and schemas"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class RetentionPolicy(BaseModel):
    """Model for version history retention policies"""
    id: int
    scope: str  # e.g., 'users', 'groups', 'projects'
    retention_days: int
    description: Optional[str]
    created_at: datetime
    modified_at: datetime

    class Config:
        """Pydantic model configuration"""
        from_attributes = True  # For SQLAlchemy compatibility
        json_schema_extra = {
            "example": {
                "id": 1,
                "scope": "users",
                "retention_days": 30,
                "description": "User version history retention policy",
                "created_at": "2024-01-01T00:00:00",
                "modified_at": "2024-01-01T00:00:00"
            }
        }

class RetentionPolicyUpdate(BaseModel):
    """Schema for updating retention policies"""
    retention_days: int
    description: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "retention_days": 60,
                "description": "Updated retention period for user versions"
            }
        }