from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Header, status

from api_gateway import logging
from api_gateway.web.api.user_service.exceptions import AuthorizationError
from api_gateway.services.user_service.lifetime import user_service_post_session
from api_gateway.services.tatcami.lifetime import tatcami_get_session
from api_gateway.web.api.tatcami.exceptions import (
    GetDevicesOnOrganizationsError, GetGeneralStatisticsError,
    GetStatisticsOnOrganizationsError, InvalidOrganizationIdError)
from api_gateway.web.exceptions import (AbstractError, BadRequest,
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
async def get_general_statistics(token: Annotated[str | None, Header()]):
    """Получение общей статистики

    Raises:
        GetGeneralStatisticsError: Ошибка при получении общей статистики с ТатЦАМи
    """

    auth = await user_service_post_session("me", headers={'Authorization': token})
    print(auth)
    if 'message' in auth:
        if (auth['message'] == 'Unauthenticated.'):
            raise AuthorizationError()

    try:
        return await tatcami_get_session("")
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
async def get_organizations_statistics(token: Annotated[str | None, Header()]):
    """Получение статистики по организациям

    Raises:
        GetStatisticsOnOrganizationsError: Ошибка при получении статистики по организациям с ТатЦАМи
    """

    auth = await user_service_post_session("me", headers={'Authorization': token})
    if 'message' in auth:
        if (auth['message'] == 'Unauthenticated.'):
            raise AuthorizationError()

    try:
        return await tatcami_get_session("organizations/")
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
async def get_devices_of_organization(token: Annotated[str | None, Header()], organization_id: UUID):
    """Получение устройств организации

    Args:
        organization_id (UUID): Идентификатор организации

    Raises:
        InvalidOrganizationIdError: Ошибка при получении id организации ТатЦАМи
        GetDevicesOnOrganizationsError: Ошибка при получении устройств организации с ТатЦАМи
    """

    auth = await user_service_post_session("me", headers={'Authorization': token})
    if 'message' in auth:
        if (auth['message'] == 'Unauthenticated.'):
            raise AuthorizationError()

    try:
        return await tatcami_get_session(f"devices/organization/{organization_id}")
    except AbstractError as error:
        if error.message == "InvalidOrganizationIdError":
            raise InvalidOrganizationIdError()
        logging.error(
            f"Error while getting organization's devices:({error.status}: {error.message})",
        )
        raise GetDevicesOnOrganizationsError()
