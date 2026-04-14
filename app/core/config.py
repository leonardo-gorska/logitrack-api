from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, validator
from typing import Optional, Any

class Settings(BaseSettings):
    PROJECT_NAME: str = "LogiTrack API"
    API_V1_STR: str = "/api/v1"
    
    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8 # 8 days
    
    # Database
    DATABASE_URL: Optional[PostgresDsn] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
