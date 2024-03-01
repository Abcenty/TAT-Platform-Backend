from uuid import UUID

from fastapi import APIRouter, status

from gateway import logging
from gateway.services.tatcami.lifetime import tatcami_get_session
from gateway.web.api.tatcami.exceptions import (
    GetDevicesOnOrganizationsError,
    GetGeneralStatisticsError, GetStatisticsOnOrganizationsError,
    InvalidOrganizationIdError)
from gateway.web.exceptions import (AbstractError, BadRequest,
                                    DetailedHTTPException)

router = APIRouter()


@router.get(
    path="/statistics",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"description": "Общая статистика с ТатЦАМи получена"},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": GetGeneralStatisticsError},
    },
)
async def get_general_statistics():
    """Получение общей статистики

    Raises:
        GetGeneralStatisticsError: Ошибка при получении общей статистики с ТатЦАМи
    """
    try:
        return await tatcami_get_session("api/v1/statistics/")
    except AbstractError as error:
        logging.error(
            f"Error while getting general statistics:({error.status}: {error.message})",
        )
        raise GetGeneralStatisticsError()


@router.get(
    path="/statistics/organizations",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "description": "Соединение со шлюзом для ТатЦАМИ установлено",
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": GetStatisticsOnOrganizationsError,
        },
    },
)
async def get_organizations_statistics():
    """Получение статистики по организациям

    Raises:
        GetStatisticsOnOrganizationsError: Ошибка при получении статистики по организациям с ТатЦАМи
    """
    try:
        return await tatcami_get_session("api/v1/statistics/organizations/")
    except AbstractError as error:
        logging.error(
            f"Error while getting statistics on organizations:({error.status}: {error.message})",
        )
        raise GetStatisticsOnOrganizationsError()


@router.get(
    path="/statistics/devices/organizations/{organization_id}",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_204_NO_CONTENT: {
            "description": "Соединение со шлюзом для ТатЦАМИ установлено",
        },
        status.HTTP_400_BAD_REQUEST: {"model": BadRequest},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": DetailedHTTPException},
    },
)
async def get_devices_of_organization(organization_id: UUID):
    """Получение устройств организации

    Args:
        organization_id (UUID): Идентификатор организации

    Raises:
        InvalidOrganizationIdError: Ошибка при получении id организации ТатЦАМи
        GetDevicesOnOrganizationsError: Ошибка при получении устройств организации с ТатЦАМи
    """
    try:
        return await tatcami_get_session(f"api/v1/statistics/organizations/{organization_id}")
    except AbstractError as error:
        if error.message == "InvalidOrganizationIdError":
            raise InvalidOrganizationIdError()
        logging.error(
            f"Error while getting organization's devices:({error.status}: {error.message})",
        )
        raise GetDevicesOnOrganizationsError()
