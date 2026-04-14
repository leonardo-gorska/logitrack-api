from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List

from app.crud.base import CRUDBase
from app.models.route import Route
from app.schemas.route import RouteCreate, RouteStatusUpdate

class CRUDRoute(CRUDBase[Route, RouteCreate, RouteStatusUpdate]):
    async def get_active_by_vehicle(self, db: AsyncSession, *, vehicle_id: str) -> List[Route]:
        query = select(Route).where(
            Route.vehicle_id == vehicle_id,
            Route.status.in_(["PENDING", "IN_TRANSIT"])
        )
        result = await db.execute(query)
        return result.scalars().all()

    async def get_active_by_driver(self, db: AsyncSession, *, driver_id: str) -> List[Route]:
        query = select(Route).where(
            Route.driver_id == driver_id,
            Route.status.in_(["PENDING", "IN_TRANSIT"])
        )
        result = await db.execute(query)
        return result.scalars().all()

route = CRUDRoute(Route)
