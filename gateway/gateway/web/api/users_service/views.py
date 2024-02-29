from fastapi import APIRouter, status
from gateway import logging
from gateway.web.api.users_service.exceptions import (

)
from gateway.services.users_service.lifetime import users_service_get_session
from uuid import UUID

from gateway.web.exceptions import AbstractError

router = APIRouter()




@router.post(
    path="/statistics",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"description": "Общая статистика с ТатЦАМи получена"},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": GetGeneralStatisticsError},
    },
)
async def check_valid_token():
    try:
        users_service_get_session("me")
    except AbstractError as error:
        logging.error(
            f"Error while getting general statistics:({error.status}: {error.message})",
        )
        raise GetGeneralStatisticsError()