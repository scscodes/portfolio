"""Membership management routes"""
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from datetime import datetime

from .models import Membership
from .schemas import (
    MembershipCreate,
    MembershipUpdate,
    MembershipResponse,
    UserMembershipResponse,
    GroupMembershipResponse
)
from .service import MembershipService
from config.database import get_db
from shared.exceptions import EntityNotFoundError, InvalidMembershipError

router = APIRouter(prefix="/memberships", tags=["memberships"])

@router.post("/users/{user_id}/memberships/{membership_id}")
def add_user_to_membership(
    user_id: int,
    membership_id: int,
    start_date: datetime = None,
    db: Session = Depends(get_db)
):
    """Add a user to a membership"""
    service = MembershipService(db)
    try:
        return service.add_user_to_membership(user_id, membership_id, start_date)
    except InvalidMembershipError:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/users/{user_id}/memberships/{membership_id}")
def remove_user_from_membership(
    user_id: int,
    membership_id: int,
    end_date: datetime = None,
    db: Session = Depends(get_db)
):
    """Remove a user from a membership"""
    service = MembershipService(db)
    try:
        service.remove_user_from_membership(user_id, membership_id, end_date)
        return {"status": "success"}
    except InvalidMembershipError:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/users/{user_id}/memberships", response_model=List[UserMembershipResponse])
def get_user_memberships(
    user_id: int,
    include_historical: bool = False,
    db: Session = Depends(get_db)
):
    """Get all memberships for a user"""
    service = MembershipService(db)
    return service.get_user_memberships(user_id, include_historical)

@router.get("/groups/{group_id}/memberships", response_model=List[GroupMembershipResponse])
def get_group_memberships(
    group_id: int,
    include_historical: bool = False,
    db: Session = Depends(get_db)
):
    """Get all memberships for a group"""
    service = MembershipService(db)
    return service.get_group_memberships(group_id, include_historical) 