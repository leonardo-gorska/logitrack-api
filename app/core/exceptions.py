from typing import Any

from fastapi import HTTPException, status

class EntityNotFoundError(HTTPException):
    def __init__(self, entity_name: str, entity_id: Any):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{entity_name} with id {entity_id} not found."
        )

class BusinessLogicError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail
        )

# we can register these cleanly in main.py if we wanted to map custom generic python exceptions
# but using HTTPException subclasses is cleaner out of the box in FastAPI for simple projects.
