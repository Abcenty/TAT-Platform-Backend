from sqlalchemy.ext.asyncio import AsyncSession

from vitacore_service.adapters.db.departments.departments_gateway import DBDepartmentsGateway
from vitacore_service.adapters.db.uow import SAUnitOfWork


def get_uow(session: AsyncSession) -> SAUnitOfWork:
    return SAUnitOfWork(session=session)


def get_db_departments_gateway(session: AsyncSession) -> DBDepartmentsGateway:
    return DBDepartmentsGateway(session=session)