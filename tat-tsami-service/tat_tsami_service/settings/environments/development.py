from pydantic_settings import SettingsConfigDict

from tat_tsami_service.settings.environments.app import AppSettings


class DevAppSettings(AppSettings):
    debug: bool = True

    model_config = SettingsConfigDict(env_file=".env.example")
