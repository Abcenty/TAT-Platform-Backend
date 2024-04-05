import logging
from typing import AsyncGenerator, Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from vitacore_service.infra.config import Settings, get_settings
from vitacore_service.infra.db.models.base import Base


async def get_engine(
    settings: Annotated[Settings, Depends(get_settings)],
) -> AsyncGenerator[AsyncEngine, None]:
    """
    Creates an asynchronous engine.

    !!! Depends from FastAPI is used; if you change the framework, you will need to change the arguments
    """
    engine = create_async_engine(
        settings.database_url,
        pool_pre_ping=True,
    )
    logging.info("Engine was created.")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        logging.info("Tables were created.")

    yield engine

    await engine.dispose()
    logging.info("Engine was disposed.")


async def get_async_sessionmaker(
    engine: Annotated[AsyncEngine, Depends(get_engine)],
) -> async_sessionmaker[AsyncSession]:
    """
    Creates an asynchronous session factory.

    !!! Depends from FastAPI is used; if you change the framework, you will need to change the arguments
    """
    session_factory = async_sessionmaker(
        engine,
        expire_on_commit=False,
        class_=AsyncSession,
    )
    logging.info("Session factory was initialized")

    return session_factory
