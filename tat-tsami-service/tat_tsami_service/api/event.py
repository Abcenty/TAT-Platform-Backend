from contextlib import asynccontextmanager

from aiohttp import ClientSession
from fastapi import FastAPI

from tat_tsami_service.api.deps import AppSettingsMarker, ClientSessionMarker
from tat_tsami_service.settings.environments.app import AppSettings


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    settings: AppSettings = app.dependency_overrides[AppSettingsMarker]() # noqa

    client = ClientSession()

    app.dependency_overrides.update(  # noqa
        {
            ClientSessionMarker: lambda: client
        }
    )

    yield

    await client.close()
