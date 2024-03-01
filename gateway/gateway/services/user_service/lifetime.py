import json
import aiohttp
from typing import Callable
from gateway.web.exceptions import AbstractError

from gateway.settings import settings


async def user_service_get_session(path: str) -> Callable:
    """Получение сессионого соединения с микросервисом user_service

    Args:
        path (str): эндпоинт, по котормоу получаем информацию с user_service

    Returns:
        _type_: Тело запроса с эндпоинта
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"{settings.user_service_service_protocol}://{settings.user_service_service_host}:{settings.user_service_service_port}/{path}",
        ) as response:
            return await response.text()


async def user_service_post_session(path: str, body: dict | None = None) -> Callable:
    """Получение сессионого соединения с микросервисом user_service

    Args:
        path (str): эндпоинт, по котормоу получаем информацию с user_service
        body (dict | None): данные для отправки

    Returns:
        _type_: Тело запроса с эндпоинта
    """
    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"{settings.user_service_service_protocol}://{settings.user_service_service_host}:{settings.user_service_service_port}/{path}",
            data=body.dict()
        ) as response:
            # raise AbstractError(status=response.status, message=json.loads(await response.text()))
            return json.loads(await response.text())
