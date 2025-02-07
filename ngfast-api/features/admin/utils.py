"""Admin utility functions"""
from datetime import datetime, timedelta
from typing import Dict, Any
from config.database import get_db

def cleanup_versions(days: int = 30) -> Dict[str, Any]:
    """
    Clean up old version history records
    
    Args:
        days: Number of days of history to keep
        
    Returns:
        Dict with cleanup results
    """
    try:
        cutoff_date = (datetime.utcnow() - timedelta(days=days)).isoformat()
        
        with get_db() as db:
            cursor = db.cursor()
            
            # Clean up user versions
            cursor.execute(
                "DELETE FROM user_versions WHERE archived_at < ?",
                (cutoff_date,)
            )
            users_deleted = cursor.rowcount
            
            # Clean up group versions
            cursor.execute(
                "DELETE FROM group_versions WHERE archived_at < ?",
                (cutoff_date,)
            )
            groups_deleted = cursor.rowcount
            
            # Clean up project versions
            cursor.execute(
                "DELETE FROM project_versions WHERE archived_at < ?",
                (cutoff_date,)
            )
            projects_deleted = cursor.rowcount
            
            return {
                "cutoff_date": cutoff_date,
                "deleted_counts": {
                    "users": users_deleted,
                    "groups": groups_deleted,
                    "projects": projects_deleted
                }
            }
            
    except Exception as e:
        print(f"Error during version cleanup: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error performing version cleanup"
        ) 