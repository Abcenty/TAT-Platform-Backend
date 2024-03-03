from json import loads
from typing import Callable

import aiohttp

from api_gateway.settings import settings


async def tatcami_get_session(path: str) -> Callable:
    """Получение сессионого соединения с микросервисом ТатЦАМи

    Args:
        path (str): эндпоинт, по котормоу получаем информацию с ТатЦАМи

    Returns:
        _type_: Тело запроса с эндпоинта
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"{settings.tatcami_service_protocol}://{settings.tatcami_service_host}:{settings.tatcami_service_port}/{path}",
        ) as response:
            return loads(await response.text())
