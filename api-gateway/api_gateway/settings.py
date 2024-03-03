import enum
from pathlib import Path
from tempfile import gettempdir
from typing import List
from dotenv import load_dotenv
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
    host: str
    port: int
    origins: List[str]
    # Включение режима отладки
    reload: bool

    # Текущее окружение
    environment: str = "prod"

    # Микросервис ТатЦАМи
    tatcami_service_protocol: str
    tatcami_service_host: str
    tatcami_service_port: int

    # Микросервис user_service
    user_service_service_protocol: str
    user_service_service_host: str
    user_service_service_port: int

    log_level: LogLevel = LogLevel.DEBUG

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
