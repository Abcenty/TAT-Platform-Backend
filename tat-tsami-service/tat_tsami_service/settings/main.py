from typing import Dict, Type

from tat_tsami_service.settings.environments.app import AppSettings
from tat_tsami_service.settings.environments.base import AppEnvTypes
from tat_tsami_service.settings.environments.development import DevAppSettings
from tat_tsami_service.settings.environments.production import ProdAppSettings

environments: Dict[str, Type[AppSettings]] = {
    AppEnvTypes.prod: ProdAppSettings,
    AppEnvTypes.dev: DevAppSettings
}


def get_app_settings(app_env: AppEnvTypes = AppEnvTypes.dev) -> AppSettings:
    return environments[app_env]()
