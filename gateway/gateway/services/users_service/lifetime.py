import aiohttp
from typing import Callable

from gateway.settings import settings


async def users_service_get_session(path: str) -> Callable:
    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"{settings.users_service_protocol}://{settings.users_service_host}:{settings.users_service_port}/{path}",
        ) as response:
            return await response.text()
