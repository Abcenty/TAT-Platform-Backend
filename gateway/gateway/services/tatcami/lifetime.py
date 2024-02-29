import aiohttp

from gateway.settings import settings


async def root():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:7001/') as response:
            return await response.text()