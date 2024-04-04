from sqlalchemy.ext.asyncio import AsyncSession

from vitacore_service.application.common.uow import UoW


class SAUnitOfWork(UoW):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()

    async def flush(self) -> None:
        await self.session.flush()
