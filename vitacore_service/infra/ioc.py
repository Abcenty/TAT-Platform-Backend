from contextlib import asynccontextmanager
from typing import AsyncContextManager

import aiohttp
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from vitacore_service.adapters.db.providers import get_db_departments_gateway, get_uow
from vitacore_service.adapters.http.providers import get_http_departments_gateway
from vitacore_service.application.departments.get_departments import GetDepartments
from vitacore_service.domain.services.departments import DepartmentsService
from vitacore_service.infra.config import get_settings
from vitacore_service.presentation.interactor_factory import InteractorFactory


class IoC(InteractorFactory):
    def __init__(self, async_session_factory: async_sessionmaker[AsyncSession]):
        self._async_session_factory = async_session_factory

    @asynccontextmanager
    async def get_departments(self) -> AsyncContextManager[GetDepartments]:
        async with self._async_session_factory() as db_session:
            async with aiohttp.ClientSession() as aiohttp_session:
                yield GetDepartments(
                    http_departments_reader=get_http_departments_gateway(aiohttp_session, get_settings()),
                    db_departments_saver=get_db_departments_gateway(db_session),
                    departments_service=DepartmentsService(),
                    uow=get_uow(db_session)
                )