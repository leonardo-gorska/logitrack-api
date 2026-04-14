from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import Optional

class DriverBase(BaseModel):
    full_name: str
    license_number: str
    is_active: bool = True

class DriverCreate(DriverBase):
    pass

class DriverUpdate(DriverBase):
    full_name: Optional[str] = None
    license_number: Optional[str] = None
    is_active: Optional[bool] = None

class DriverInDBBase(DriverBase):
    id: UUID
    model_config = ConfigDict(from_attributes=True)

class Driver(DriverInDBBase):
    pass
