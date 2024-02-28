from tat_tsami_service.settings.environments.app import AppSettings


class ProdAppSettings(AppSettings):
    debug: bool = False
