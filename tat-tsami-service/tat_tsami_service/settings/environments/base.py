import enum

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppEnvTypes(str, enum.Enum):
    prod: str = "prod"
    dev: str = "dev"


class BaseAppSettings(BaseSettings):
    app_env: AppEnvTypes = AppEnvTypes.prod

    model_config = SettingsConfigDict(
        env_file=".env",
        validate_assignment=True,
    )
