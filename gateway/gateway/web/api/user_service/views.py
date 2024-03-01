from fastapi import APIRouter, status

from gateway import logging
from gateway.services.tatcami.lifetime import tatcami_post_session
from gateway.web.api.tatcami.exceptions import AuthorizationError
from gateway.web.api.user_service.schema import Auth
from gateway.web.exceptions import AbstractError

router = APIRouter()


@router.post(
    path='/auth',
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"description": "Токен авторизации получен"},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": AuthorizationError},
    }
)
async def auth(auth_data: Auth):
    """Авторизация

    Raises:
        AuthorizationError: Ошибка при получении токена авторизации
    """
    try:
        await tatcami_post_session("api/v1/auth/", auth_data)
    except AbstractError as error:
        logging.error(
            f"Error while authorization:({error.status}: {error.message})",
        )
        raise AuthorizationError()
