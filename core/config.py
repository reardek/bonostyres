import logging
import os
from enum import Enum
from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings, PostgresDsn

from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


class EnvironmentEnum(str, Enum):
    LOCAL = "local"


class GlobalConfig(BaseSettings):
    TITLE: str = "F1 RESTful API"

    DB_NAME: str = 'bonostyres'
    DB_USER: str = 'deployer'
    DB_PASSWORD: str = os.environ.get('DB_PASSWORD')
    ENVIRONMENT: EnvironmentEnum
    DEBUG: bool = False
    TESTING: bool = False
    TIMEZONE: str = "UTC"

    DATABASE_URL: Optional[
        PostgresDsn
    ] = f"postgresql://deployer:{DB_PASSWORD}@127.0.0.1:5432/{DB_NAME}"
    DB_ECHO_LOG: bool = False

    @property
    def async_database_url(self) -> Optional[str]:
        return (
            self.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
            if self.DATABASE_URL
            else self.DATABASE_URL
        )

    API_V1_STR = "/v1"

    class Config:
        case_sensitive = True


class LocalConfig(GlobalConfig):
    """Local configurations."""

    DEBUG: bool = True
    ENVIRONMENT: EnvironmentEnum = EnvironmentEnum.LOCAL


class FactoryConfig:
    def __init__(self, environment: Optional[str]):
        self.environment = environment

    def __call__(self) -> GlobalConfig:
        return LocalConfig()
    


@lru_cache()
def get_configuration() -> GlobalConfig:
    return FactoryConfig(os.environ.get("ENVIRONMENT"))()


settings = get_configuration()