from json import loads
from typing import Callable, Optional

import aiohttp

from api_gateway.settings import settings


async def vitacore_get_session(path: str, params: Optional[dict] = None) -> Callable:
    """Получение сессионого соединения с микросервисом ViteCore

    Args:
        path (str): эндпоинт, по котормоу получаем информацию с ViteCore
        params (Optional[dict]): Параметры запроса

    Returns:
        _type_: Тело запроса с эндпоинта
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"{settings.vitacore_service_protocol}://{settings.vitacore_service_host}:{settings.vitacore_service_port}/{path}",
            params=params,
        ) as response:
            return loads(await response.text())
