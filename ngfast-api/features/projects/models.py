"""Project domain models and schemas"""
from datetime import datetime
from typing import Dict, Any, Optional
from pydantic import BaseModel

class Project(BaseModel):
    """Base project model"""
    id: int
    name: str
    description: Optional[str]
    properties: Dict[str, Any]
    created_at: datetime
    modified_at: datetime
    evaluated_at: datetime

class ProjectVersion(Project):
    """Project version history model"""
    project_id: int
    archived_at: datetime

class ProjectUpdate(BaseModel):
    """Schema for project updates"""
    name: str
    description: Optional[str]
    properties: Dict[str, Any]

    class Config:
        schema_extra = {
            "example": {
                "name": "Project Name",
                "description": "Project Description",
                "properties": {
                    "status": "active",
                    "priority": "high",
                    "category": "development",
                    "tags": ["api", "backend"]
                }
            }
        }
