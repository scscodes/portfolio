"""Group management routes"""
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session

from .models import GroupDB
from features.memberships.models import GroupMembershipHistory
from .schemas import (
    Group,
    GroupCreate,
    GroupUpdate,
    GroupHistory as GroupHistorySchema,
    GroupMemberships
)
from .service import GroupService
from config.database import get_db
from shared.exceptions import EntityNotFoundError, CyclicGroupError

router = APIRouter(prefix="/groups", tags=["groups"])

@router.get("/", response_model=List[Group])
def get_groups(db: Session = Depends(get_db)):
    """Get all groups"""
    service = GroupService(db)
    return service.get_all_groups()

@router.post("/", response_model=Group)
def create_group(group: GroupCreate, db: Session = Depends(get_db)):
    """Create a new group"""
    service = GroupService(db)
    try:
        return service.create_group(group)
    except CyclicGroupError:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{group_id}", response_model=Group)
def get_group(group_id: int, db: Session = Depends(get_db)):
    """Get a specific group by ID"""
    service = GroupService(db)
    group = service.get_group_by_id(group_id)
    if not group:
        raise EntityNotFoundError("Group", group_id)
    return group

@router.patch("/{group_id}", response_model=Group)
def update_group(group_id: int, group_update: GroupUpdate, db: Session = Depends(get_db)):
    """Update a group"""
    service = GroupService(db)
    try:
        return service.update_group(group_id, group_update)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{group_id}/history", response_model=List[GroupHistorySchema])
def get_group_history(group_id: int, db: Session = Depends(get_db)):
    """Get version history for a group"""
    service = GroupService(db)
    history = service.get_group_history(group_id)
    if not history:
        raise EntityNotFoundError("Group", group_id)
    return history

@router.get("/{group_id}/members", response_model=GroupMemberships)
def get_group_members(group_id: int, db: Session = Depends(get_db)):
    """Get all members of a group"""
    service = GroupService(db)
    return service.get_group_members(group_id)
