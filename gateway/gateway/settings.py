import enum
from pathlib import Path
from tempfile import gettempdir
from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict

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
    host: str = "127.0.0.1"
    port: int = 7070
    origins: List[str] = ["*"]
    # Количество воркеров uvicorn
    workers_count: int = 3
    # Включение режима отладки
    reload: bool = True

    # Текущее окружение
    environment: str = "prod"

    # Микросервис ТатЦАМи
    tatcami_service_protocol: str = "http"
    tatcami_service_host: str = "127.0.0.1"
    tatcami_service_port: int = 7001

    log_level: LogLevel = LogLevel.DEBUG

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="GATEWAY_",
        env_file_encoding="utf-8",
    )


settings = Settings()
