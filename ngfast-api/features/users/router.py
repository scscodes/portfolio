"""User management routes"""
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session

from .models import UserDB
from .schemas import (
    User,
    UserCreate,
    UserUpdate,
    UserHistory as UserHistorySchema
)
from .service import UserService
from config.database import get_db
from shared.exceptions import EntityNotFoundError

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[User])
def get_users(db: Session = Depends(get_db)):
    """Get all users"""
    service = UserService(db)
    return service.get_all_users()

@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user"""
    service = UserService(db)
    return service.create_user(user)

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Get a specific user by ID"""
    service = UserService(db)
    user = service.get_user_by_id(user_id)
    if not user:
        raise EntityNotFoundError("User", user_id)
    return user

@router.patch("/{user_id}", response_model=User)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    """Update a user"""
    service = UserService(db)
    try:
        return service.update_user(user_id, user_update)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{user_id}/history", response_model=List[UserHistorySchema])
def get_user_history(user_id: int, db: Session = Depends(get_db)):
    """Get version history for a user"""
    service = UserService(db)
    history = service.get_user_history(user_id)
    if not history:
        raise EntityNotFoundError("User", user_id)
    return history
