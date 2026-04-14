from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.db.base import Base

class Driver(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    full_name = Column(String, nullable=False)
    license_number = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)

    routes = relationship("Route", back_populates="driver")
