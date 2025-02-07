"""Common exception types"""
from fastapi import HTTPException

class EntityNotFoundError(HTTPException):
    """Raised when an entity is not found"""
    def __init__(self, entity_type: str, entity_id: str):
        super().__init__(
            status_code=404,
            detail=f"{entity_type} with id {entity_id} not found"
        )

class ValidationError(HTTPException):
    """Raised for validation failures"""
    def __init__(self, message: str):
        super().__init__(
            status_code=422,
            detail=message
        )

"""Custom exceptions for the application"""
class MembershipError(HTTPException):
    """Base class for membership-related errors"""
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)

class CyclicGroupError(MembershipError):
    """Raised when a cyclic group relationship is detected"""
    def __init__(self):
        super().__init__("Cyclic group relationship detected")

class InvalidMembershipError(MembershipError):
    """Raised when an invalid membership operation is attempted"""
    pass

class TemporaryAccessError(MembershipError):
    """Raised when temporary access rules are violated"""
    pass 