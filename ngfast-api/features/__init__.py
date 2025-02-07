"""Features package containing vertical slices of functionality"""

"""
Features package initialization
"""
from features.users.models import UserDB
from features.users.schemas import User
from features.groups.models import GroupDB
from features.groups.schemas import Group

# Import additional models here as needed

__all__ = ['UserDB', 'User', 'GroupDB', 'Group'] 