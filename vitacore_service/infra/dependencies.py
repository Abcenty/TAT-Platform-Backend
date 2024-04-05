from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker

from vitacore_service.infra.db.main import get_async_sessionmaker
from vitacore_service.infra.ioc import IoC
from vitacore_service.presentation.interactor_factory import InteractorFactory


def get_ioc(
    session_factory: Annotated[async_sessionmaker, Depends(get_async_sessionmaker)],
) -> InteractorFactory:
    return IoC(session_factory)


ioc_dep = Annotated[InteractorFactory, Depends(get_ioc)]
