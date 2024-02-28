from uuid import UUID

from aiohttp import ClientSession
from fastapi import APIRouter, Query, Depends

from tat_tsami_service.api.deps import ClientSessionMarker, AppSettingsMarker
from tat_tsami_service.schemas import (
    StatisticsSchema,
    StatisticsOrganizationsSchema,
    StatisticsDevicesSchema
)
from tat_tsami_service.services import (
    get_statistics,
    get_statistics_organizations,
    get_statistics_devices
)
from tat_tsami_service.settings.environments.app import AppSettings

router = APIRouter()


@router.get("/", response_model=StatisticsSchema)
async def read_statistics(
    client: ClientSession = Depends(ClientSessionMarker),
    settings: AppSettings = Depends(AppSettingsMarker)
):
    return await get_statistics(client=client, settings=settings)


@router.get(
    "/organizations/",
    response_model=StatisticsOrganizationsSchema
)
async def read_organizations(
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=10),
    client: ClientSession = Depends(ClientSessionMarker),
    settings: AppSettings = Depends(AppSettingsMarker)
):
    return await get_statistics_organizations(
        offset=offset,
        limit=limit,
        client=client,
        settings=settings
    )


@router.get("/devices/organization/{id}", response_model=StatisticsDevicesSchema)
async def read_devices(
    id: UUID,
    client: ClientSession = Depends(ClientSessionMarker),
    settings: AppSettings = Depends(AppSettingsMarker)
):
    return await get_statistics_devices(
        organization_id=id,
        client=client,
        settings=settings
    )
