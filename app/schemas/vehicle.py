from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID
from typing import Optional

class VehicleBase(BaseModel):
    license_plate: str = Field(..., pattern=r"^[A-Z]{3}-?\d{1}[A-Z0-9]{1}\d{2}$|^[A-Z]{3}-?\d{4}$")
    model: str
    capacity_kg: float = Field(..., gt=0)
    is_available: bool = True

class VehicleCreate(VehicleBase):
    pass

class VehicleUpdate(VehicleBase):
    license_plate: Optional[str] = None
    model: Optional[str] = None
    capacity_kg: Optional[float] = None
    is_available: Optional[bool] = None

class VehicleInDBBase(VehicleBase):
    id: UUID
    model_config = ConfigDict(from_attributes=True)

class Vehicle(VehicleInDBBase):
    pass
