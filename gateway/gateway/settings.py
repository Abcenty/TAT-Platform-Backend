import enum
from pathlib import Path
from tempfile import gettempdir
from typing import List
from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

TEMP_DIR = Path(gettempdir())


class LogLevel(str, enum.Enum):  # noqa: WPS600
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """Настройки приложения."""

    # Адрес для запуска приложения
    host: str = os.getenv("GATEWAY_HOST")
    port: int = os.getenv("GATEWAY_PORT")
    origins: List[str] = ["*"]
    # Количество воркеров uvicorn
    workers_count: int = os.getenv("GATEWAY_WORKERS_COUNT")
    # Включение режима отладки
    reload: bool = os.getenv("GATEWAY_RELOAD")

    # Текущее окружение
    environment: str = "prod"

    # Микросервис ТатЦАМи
    tatcami_service_protocol: str = os.getenv("GATEWAY_TATCAMI_SERVICE_PROTOCOL")
    tatcami_service_host: str = os.getenv("GATEWAY_TATCAMI_SERVICE_HOST")
    tatcami_service_port: int = os.getenv("GATEWAY_TATCAMI_SERVICE_PORT")

    log_level: LogLevel = LogLevel.DEBUG

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="GATEWAY_",
        env_file_encoding="utf-8",
    )


settings = Settings()
