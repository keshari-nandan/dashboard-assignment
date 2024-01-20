import os
import logging
from urllib.parse import quote, quote_plus
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

log = logging.getLogger("uvicorn")

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    environment: str = os.getenv('APP_ENV', 'production')
    testing: bool = False

    APP_NAME: str = os.getenv('APP_NAME', 'FastApi')
    VERSION: str = os.getenv('APP_VERSION', '0.0.0')
    LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'DEBUG')
    DEBUG: bool = os.getenv('DEBUG', True)

    USE_SQLITE_DB: str = os.getenv("USE_SQLITE_DB", False)

    DB_USER: str = os.getenv('MYSQL_USER')
    DB_PASSWORD: str = os.getenv('MYSQL_PASSWORD')
    DB_NAME: str = os.getenv('MYSQL_DB')
    DB_HOST: str = os.getenv('MYSQL_SERVER')
    DB_PORT: str = os.getenv('MYSQL_PORT')
    DATABASE_URL: str = f"mysql+pymysql://{DB_USER}:%s@{DB_HOST}:{DB_PORT}/{DB_NAME}" % quote_plus(DB_PASSWORD)
    DATABASE_MIGRATION_URL: str = f"mysql+pymysql://{DB_USER}:%s@{DB_HOST}:{DB_PORT}/{DB_NAME}" % quote(DB_PASSWORD).replace("%", "%%")

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    
    # JWT Config
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1200
    JWT_ALGORITHM: str = "HS256"
    JWT_SECRET: str = os.getenv("JWT_SECRET", 'secret')


# @lru_cache()
def get_settings() -> Settings:
    log.info("Loading config settings from the environment...")
    return Settings()
