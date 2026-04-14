from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.Driver)
async def create_driver(
    *,
    db: AsyncSession = Depends(deps.get_db),
    driver_in: schemas.DriverCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new driver.
    """
    driver = await crud.driver.create(db=db, obj_in=driver_in)
    return driver

@router.get("/", response_model=List[schemas.Driver])
async def read_drivers(
    db: AsyncSession = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve drivers.
    """
    drivers = await crud.driver.get_multi(db, skip=skip, limit=limit)
    return drivers
