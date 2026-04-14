from sqlalchemy import Column, String, Float, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.db.base import Base

class Vehicle(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    license_plate = Column(String(10), unique=True, index=True, nullable=False)
    model = Column(String, nullable=False)
    capacity_kg = Column(Float, nullable=False)
    is_available = Column(Boolean, default=True)

    # Relationships
    routes = relationship("Route", back_populates="vehicle")
