from pydantic_settings import SettingsConfigDict

from tat_tsami_service.settings.environments.base import BaseAppSettings


class AppSettings(BaseAppSettings):
    debug: bool = False

    server_host: str = "127.0.0.1"
    server_port: int = 8080

    tat_tsami_service_base_url: str

    model_config = SettingsConfigDict(env_file=".env")
