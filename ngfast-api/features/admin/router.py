"""Admin management routes"""
from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from datetime import datetime, timedelta
from .models import RetentionPolicy, RetentionPolicyUpdate
from config.database import get_db
from .utils import cleanup_versions

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/retention", response_model=List[RetentionPolicy])
def get_retention_policies():
    """Get all retention policies"""
    try:
        with get_db() as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM retention_policies")
            policies = cursor.fetchall()
            return [RetentionPolicy(**policy) for policy in policies]
    except Exception as e:
        print(f"Error fetching retention policies: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error fetching retention policies"
        )

@router.put("/retention/{scope}", response_model=RetentionPolicy)
def update_retention_policy(scope: str, update_data: RetentionPolicyUpdate):
    """Update retention period for a specific scope"""
    try:
        with get_db() as db:
            cursor = db.cursor()
            
            # Update policy
            cursor.execute(
                """
                UPDATE retention_policies 
                SET retention_days = ?, 
                    description = COALESCE(?, description),
                    modified_at = ? 
                WHERE scope = ?
                RETURNING *
                """,
                (
                    update_data.retention_days,
                    update_data.description,
                    datetime.utcnow().isoformat(),
                    scope
                )
            )
            
            updated = cursor.fetchone()
            if not updated:
                raise HTTPException(
                    status_code=404,
                    detail=f"Retention policy not found for scope: {scope}"
                )
            
            # Trigger cleanup with new retention period
            cleanup_versions(update_data.retention_days)
            
            return RetentionPolicy(**updated)
            
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error updating retention policy: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error updating retention policy"
        ) 