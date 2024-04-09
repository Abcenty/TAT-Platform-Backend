from functools import lru_cache, cached_property

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="",
        case_sensitive=False,
        env_file=".env",
        env_file_encoding="utf-8",
        frozen=True,
    )

    postgres_db: str
    postgres_user: str
    postgres_password: str
    postgres_host: str = "postgres"
    postgres_port: int = 5432

    vitacore_protocol: str = "http"
    vitacore_host: str
    vitacore_port: int = 80

    service_host: str = "0.0.0.0"
    service_port: int = 8001

    @cached_property
    def vitacore_url(self) -> str:
        return f"{self.vitacore_protocol}://{self.vitacore_host}:{self.vitacore_port}/"

    @cached_property
    def database_url(self) -> URL:
        return URL.create(
            drivername="postgresql+asyncpg",
            host=self.postgres_host,
            port=self.postgres_port,
            username=self.postgres_user,
            password=self.postgres_password,
            database=self.postgres_db,
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()
