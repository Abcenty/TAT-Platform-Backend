from contextlib import asynccontextmanager
from typing import AsyncContextManager

import aiohttp
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from vitacore_service.adapters.db.providers import (
    get_db_departments_gateway,
    get_uow,
    get_db_patients_gateway,
    get_db_positions_gateway,
    get_db_workers_gateway,
)
from vitacore_service.adapters.http.providers import (
    get_http_departments_gateway,
    get_http_patients_gateway,
    get_http_workers_gateway,
)
from vitacore_service.application.departments.get_departments import GetDepartments
from vitacore_service.application.patients.find_patients import FindPatients
from vitacore_service.application.patients.get_patient import GetPatient
from vitacore_service.application.workers.get_workers import GetWorkers
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
                    http_departments_reader=get_http_departments_gateway(
                        aiohttp_session,
                        get_settings(),
                    ),
                    db_departments_saver=get_db_departments_gateway(db_session),
                    uow=get_uow(db_session),
                )

    @asynccontextmanager
    async def get_workers_by_department(self) -> AsyncContextManager[GetWorkers]:
        async with self._async_session_factory() as db_session:
            async with aiohttp.ClientSession() as aiohttp_session:
                yield GetWorkers(
                    http_workers_reader=get_http_workers_gateway(
                        aiohttp_session,
                        get_settings(),
                    ),
                    db_positions_saver=get_db_positions_gateway(db_session),
                    db_workers_saver=get_db_workers_gateway(db_session),
                    uow=get_uow(db_session),
                )

    @asynccontextmanager
    async def get_patient(self) -> AsyncContextManager[GetPatient]:
        async with self._async_session_factory() as db_session:
            async with aiohttp.ClientSession() as aiohttp_session:
                yield GetPatient(
                    http_patients_reader=get_http_patients_gateway(
                        aiohttp_session,
                        get_settings(),
                    ),
                    db_patients_saver=get_db_patients_gateway(db_session),
                    uow=get_uow(db_session),
                )

    @asynccontextmanager
    async def find_patients(self) -> AsyncContextManager[FindPatients]:
        async with self._async_session_factory() as db_session:
            async with aiohttp.ClientSession() as aiohttp_session:
                yield FindPatients(
                    http_patients_reader=get_http_patients_gateway(
                        aiohttp_session,
                        get_settings(),
                    ),
                    db_patients_saver=get_db_patients_gateway(db_session),
                    uow=get_uow(db_session),
                )
