from typing import Optional
from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from enum import Enum

from .vehicle import Vehicle
from .driver import Driver

class RouteStatus(str, Enum):
    PENDING = "PENDING"
    IN_TRANSIT = "IN_TRANSIT"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"

class RouteBase(BaseModel):
    origin: str
    destination: str
    distance_km: float
    notes: Optional[str] = None

class RouteCreate(RouteBase):
    pass

class RouteAssign(BaseModel):
    vehicle_id: UUID
    driver_id: UUID

class RouteStatusUpdate(BaseModel):
    status: RouteStatus

class RouteInDBBase(RouteBase):
    id: UUID
    status: RouteStatus
    created_at: datetime
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    vehicle_id: Optional[UUID] = None
    driver_id: Optional[UUID] = None

    model_config = ConfigDict(from_attributes=True)

class Route(RouteInDBBase):
    vehicle: Optional[Vehicle] = None
    driver: Optional[Driver] = None
