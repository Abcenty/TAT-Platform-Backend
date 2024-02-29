from uuid import UUID

from aiohttp import ClientSession

from tat_tsami_service.schemas import (
    StatisticsSchema,
    StatisticsOrganizationsSchema,
    StatisticsOrganizationSchema,
    StatisticsDevicesSchema,
    StatisticsCountDeviceSchema,
    StatisticsAgeDeviceSchema,
    StatisticsCountStudiesDeviceSchema,
)
from tat_tsami_service.settings.environments.app import AppSettings

TAT_TSAMI_SERVICE_URL = "{base_url}/medical/statistics/{endpoint}"


async def get_statistics(
    *,
    client: ClientSession,
    settings: AppSettings,
) -> StatisticsSchema:
    async with client.get(
        url=TAT_TSAMI_SERVICE_URL.format(
            base_url=settings.tat_tsami_service_base_url,
            endpoint="",
        ),
    ) as response:
        response.raise_for_status()

        json = await response.json()

        return StatisticsSchema(
            count_patients=json["count_patients"],
            count_studies=json["count_studies"],
            total_disk_size=json["total_disk_size"],
        )


async def get_statistics_organizations(
    *,
    offset: int,
    limit: int,
    client: ClientSession,
    settings: AppSettings,
) -> StatisticsOrganizationsSchema:
    async with client.get(
        url=TAT_TSAMI_SERVICE_URL.format(
            base_url=settings.tat_tsami_service_base_url,
            endpoint="organizations",
        ),
        params={"offset": offset, "limit": limit},
    ) as response:
        response.raise_for_status()

        json = await response.json()

        return StatisticsOrganizationsSchema(
            total=json["total"],
            organizations=[
                StatisticsOrganizationSchema(
                    id=UUID(organization["id"]),
                    name=organization["name"],
                    addresses=organization["addresses"],
                    device_count=organization["device_count"],
                )
                for organization in json["organizations"]
            ],
        )


async def get_statistics_devices(
    *,
    organization_id: UUID,
    client: ClientSession,
    settings: AppSettings,
) -> StatisticsDevicesSchema:
    async with client.get(
        url=TAT_TSAMI_SERVICE_URL.format(
            base_url=settings.tat_tsami_service_base_url,
            endpoint=f"devices/organization/{organization_id}",
        ),
    ) as response:
        response.raise_for_status()

        json = await response.json()

        return StatisticsDevicesSchema(
            count_devices=[
                StatisticsCountDeviceSchema(
                    modality=count_device["modality"],
                    value=count_device["value"],
                )
                for count_device in json["count_devices"]
            ],
            age_devices=[
                StatisticsAgeDeviceSchema(
                    modality=age_device["modality"],
                    count=age_device["count"],
                    group_index=age_device["group_index"],
                )
                for age_device in json["age_devices"]
            ],
            count_studies_devices=[
                StatisticsCountStudiesDeviceSchema(
                    modality=count_studies_device["modality"],
                    value=count_studies_device["value"],
                )
                for count_studies_device in json["count_studies_devices"]
            ],
        )
