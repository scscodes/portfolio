"""SQL queries for group operations"""

INSERT_GROUP = """
    INSERT INTO groups (
        name, members, properties,
        created_at, modified_at, evaluated_at
    ) VALUES (?, ?, ?, ?, ?, ?)
"""

INSERT_GROUP_VERSION = """
    INSERT INTO group_versions (
        group_id, name, members,
        properties, created_at, modified_at,
        evaluated_at, archived_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

"""Database queries for group domain"""
from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import List, Optional

from .models import GroupDB, GroupVersion
from .schemas import GroupCreate, GroupUpdate

class GroupQueries:
    def __init__(self, db: Session):
        self.db = db

    def get_all_groups(self) -> List[GroupDB]:
        """Get all groups"""
        return self.db.query(GroupDB).all()

    def get_group_by_id(self, group_id: int) -> Optional[GroupDB]:
        """Get group by ID"""
        return self.db.query(GroupDB).filter(GroupDB.group_id == group_id).first()

    def create_group(self, group_data: GroupCreate) -> GroupDB:
        """Create a new group"""
        db_group = GroupDB(
            group_name=group_data.group_name,
            description=group_data.description,
            properties=group_data.properties
        )
        self.db.add(db_group)
        self.db.commit()
        self.db.refresh(db_group)
        return db_group

    def update_group(self, group_id: int, group_data: GroupUpdate) -> Optional[GroupDB]:
        """Update group details"""
        group = self.get_group_by_id(group_id)
        if not group:
            return None

        update_data = group_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(group, key, value)

        self.db.commit()
        self.db.refresh(group)
        return group

    def get_group_history(self, group_id: int) -> List[GroupVersion]:
        """Get version history for a group"""
        return self.db.query(GroupVersion)\
            .filter(GroupVersion.group_id == group_id)\
            .order_by(GroupVersion.version.desc())\
            .all()

    def get_group_version(self, group_id: int, version_id: int) -> Optional[GroupVersion]:
        """Get specific version of a group"""
        return self.db.query(GroupVersion)\
            .filter(
                GroupVersion.group_id == group_id,
                GroupVersion.id == version_id
            ).first() 