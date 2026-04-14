from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from app import crud, models, schemas
from app.api import deps
from app.services import dispatch

router = APIRouter()

@router.post("/", response_model=schemas.Route)
async def create_route(
    *,
    db: AsyncSession = Depends(deps.get_db),
    route_in: schemas.RouteCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new route (PENDING by default).
    """
    route = await crud.route.create(db=db, obj_in=route_in)
    return route

@router.get("/", response_model=List[schemas.Route])
async def read_routes(
    db: AsyncSession = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve routes.
    """
    routes = await crud.route.get_multi(db, skip=skip, limit=limit)
    return routes

@router.post("/{route_id}/dispatch", response_model=schemas.Route)
async def dispatch_route(
    *,
    db: AsyncSession = Depends(deps.get_db),
    route_id: UUID,
    assign_in: schemas.RouteAssign,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Dispatch a route by assigning a vehicle and driver.
    Changes status to IN_TRANSIT.
    """
    route = await dispatch.assign_route_dispatch(
        db=db, 
        route_id=route_id, 
        vehicle_id=assign_in.vehicle_id, 
        driver_id=assign_in.driver_id
    )
    return route

@router.post("/{route_id}/finalize", response_model=schemas.Route)
async def finalize_route(
    *,
    db: AsyncSession = Depends(deps.get_db),
    route_id: UUID,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Finalize a route. 
    Changes status to DELIVERED and frees up the vehicle.
    """
    route = await dispatch.finalize_route(db=db, route_id=route_id)
    return route
