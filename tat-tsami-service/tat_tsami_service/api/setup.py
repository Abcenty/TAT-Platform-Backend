from fastapi import FastAPI

from tat_tsami_service.api.deps import AppSettingsMarker
from tat_tsami_service.api.endpoints.setup import init_endpoints
from tat_tsami_service.api.event import lifespan
from tat_tsami_service.api.exceptions import init_exceptions
from tat_tsami_service.settings.environments.app import AppSettings


def register_app(settings: AppSettings) -> FastAPI:
    app = FastAPI(
        debug=settings.debug,
        lifespan=lifespan
    )

    init_endpoints(app=app)
    init_exceptions(app=app)

    app.dependency_overrides.update( # noqa
        {
            AppSettingsMarker: lambda: settings
        }
    )

    return app
