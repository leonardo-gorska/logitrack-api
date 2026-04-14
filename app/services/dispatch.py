from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from uuid import UUID

from app import crud
from app.models.route import RouteStatus
from app.core.exceptions import BusinessLogicError

async def assign_route_dispatch(
    db: AsyncSession, *, route_id: UUID, vehicle_id: UUID, driver_id: UUID
):
    """
    Complex logic to assign a driver and a vehicle to a pending route.
    """
    route = await crud.route.get(db, id=route_id)
    if not route:
        raise BusinessLogicError("Route not found")
    
    if route.status != RouteStatus.PENDING:
        raise BusinessLogicError("Can only dispatch PENDING routes")
    
    vehicle = await crud.vehicle.get(db, id=vehicle_id)
    if not vehicle or not vehicle.is_available:
        raise BusinessLogicError("Vehicle not found or unavailable")
    
    driver = await crud.driver.get(db, id=driver_id)
    if not driver or not driver.is_active:
        raise BusinessLogicError("Driver not found or inactive")
    
    # Check if vehicle is already occupied
    active_v_routes = await crud.route.get_active_by_vehicle(db, vehicle_id=vehicle_id)
    if active_v_routes:
        raise BusinessLogicError("Vehicle is currently occupied in another active route")

    # Check if driver is already occupied
    active_d_routes = await crud.route.get_active_by_driver(db, driver_id=driver_id)
    if active_d_routes:
        raise BusinessLogicError("Driver is currently occupied in another active route")

    # Update route
    route.vehicle_id = vehicle_id
    route.driver_id = driver_id
    route.status = RouteStatus.IN_TRANSIT
    route.started_at = datetime.utcnow()
    
    db.add(route)
    
    # Update vehicle status (optional logic, but makes sense for logistics)
    vehicle.is_available = False
    db.add(vehicle)

    await db.commit()
    await db.refresh(route)
    return route

async def finalize_route(db: AsyncSession, *, route_id: UUID):
    route = await crud.route.get(db, id=route_id)
    if not route:
        raise BusinessLogicError("Route not found")
    
    if route.status != RouteStatus.IN_TRANSIT:
        raise BusinessLogicError("Can only finalize IN_TRANSIT routes")

    # Update route
    route.status = RouteStatus.DELIVERED
    route.completed_at = datetime.utcnow()
    db.add(route)

    # Free the vehicle
    if route.vehicle_id:
        vehicle = await crud.vehicle.get(db, id=route.vehicle_id)
        if vehicle:
            vehicle.is_available = True
            db.add(vehicle)
    
    await db.commit()
    await db.refresh(route)
    return route
