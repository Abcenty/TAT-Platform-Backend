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
    port: int = 8000
    origins: List[str] = ["*"]
    # Количество воркеров uvicorn
    workers_count: int = 1
    # Включение режима отладки
    reload: bool = False

    # Текущее окружение
    environment: str = "prod"

    # Микросервис ТАТЦАМИ
    account_tatcami_host: str = "127.0.0.1"
    account_tatcami_port: int = 50051

    log_level: LogLevel = LogLevel.DEBUG

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="BACKEND_",
        env_file_encoding="utf-8",
    )


settings = Settings()
