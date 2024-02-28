from fastapi import FastAPI
from importlib import metadata
from fastapi.responses import UJSONResponse
from web.api.router import api_router


app = FastAPI(
    title="gateway",
    version=metadata.version("gateway"),
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
    default_response_class=UJSONResponse,
)

app.include_router(router=api_router, prefix="/api")