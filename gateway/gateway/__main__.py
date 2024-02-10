from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from importlib import metadata
from gateway.logging import configure_logging
from gateway.web.api.router import api_router


configure_logging()
app = FastAPI(
        title="gateway",
        version=metadata.version("gateway"),
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

# Main router for the API.
app.include_router(router=api_router, prefix="/api")