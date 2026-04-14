from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.api_v1.api import api_router
from app.core.exceptions import BusinessLogicError, EntityNotFoundError

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For production, read from settings
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(BusinessLogicError)
async def business_logic_exception_handler(request: Request, exc: BusinessLogicError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail, "type": "business_logic_error"},
    )

@app.exception_handler(EntityNotFoundError)
async def not_found_exception_handler(request: Request, exc: EntityNotFoundError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail, "type": "not_found_error"},
    )

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok", "app": settings.PROJECT_NAME}

app.include_router(api_router, prefix=settings.API_V1_STR)
