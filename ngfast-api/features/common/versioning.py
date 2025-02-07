"""Common versioning functionality"""
from datetime import datetime
from typing import Dict, Any
from sqlalchemy import event, Column, DateTime, Integer
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declared_attr
from config.database import Base

def detect_changes(old_dict: Dict[str, Any], new_dict: Dict[str, Any]) -> bool:
    """
    Compare two dictionaries to detect meaningful changes
    Ignores timestamp fields
    """
    skip_fields = {'modified_at', 'evaluated_at', 'current_version'}
    
    old = {k: v for k, v in old_dict.items() if k not in skip_fields}
    new = {k: v for k, v in new_dict.items() if k not in skip_fields}
    
    return old != new

@event.listens_for(Session, 'before_flush')
def handle_version_changes(session, context, instances):
    """
    SQLAlchemy event listener to handle version changes
    Creates new versions when detecting changes in versioned models
    """
    for obj in session.dirty:
        if not session.is_modified(obj):
            continue
            
        if hasattr(obj, 'create_version'):
            # Get the current state of the object
            current_state = {c.key: getattr(obj, c.key) 
                           for c in obj.__table__.columns}
            
            # Get the previous state
            previous_state = session.get_original_state(obj)
            
            # Check for meaningful changes
            if detect_changes(previous_state, current_state):
                # Create new version
                obj.create_version(session)
                obj.modified_at = datetime.utcnow() 

class VersionedBase(Base):
    """
    Base class for models that require version history tracking
    Automatically adds created_at, modified_at, and version columns
    """
    __abstract__ = True

    @declared_attr
    def created_at(cls):
        return Column(DateTime, nullable=False, default=datetime.utcnow)

    @declared_attr
    def modified_at(cls):
        return Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    @declared_attr
    def version(cls):
        return Column(Integer, nullable=False, default=1)

    def create_version(self, session):
        """
        Creates a new version of the record
        To be implemented by child classes if needed
        """
        self.version += 1
        self.modified_at = datetime.utcnow() 