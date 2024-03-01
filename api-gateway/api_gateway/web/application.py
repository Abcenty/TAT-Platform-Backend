from importlib import metadata
import aiohttp
from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from api_gateway.logging import configure_logging
from api_gateway.web.api.router import api_router


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    configure_logging()
    app = FastAPI(
        title="gateway",
        # version=metadata.version("gateway"), #TODO Определить и вставить корреткную версию метаданных
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    # Adds startup and shutdown events.
    session = None

    @app.on_event("startup")
    async def _startup_event():
        global session
        session = aiohttp.ClientSession()

    @app.on_event("shutdown")
    async def _shutdown_event():
        await session.close()

    # Main router for the API.
    app.include_router(router=api_router, prefix="/api")

    return app
