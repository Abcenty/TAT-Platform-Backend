from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from vitacore_service.adapters.db.departments.departments_converter import (
    department_dto_to_db,
)
from vitacore_service.application.common.departments_gateway import DepartmentSaver
from vitacore_service.domain.models.departments import DepartmentDTO
from vitacore_service.infra.db.models import Department


class DBDepartmentsGateway(DepartmentSaver):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, department: DepartmentDTO) -> None:
        db_department = department_dto_to_db(department)

        self.session.add(db_department)
        await self.session.flush([db_department])

    async def create_bulk(self, departments: list[DepartmentDTO]) -> None:
        """
        Adds several organizations to the database. When there is a conflict, an update occurs.

        !!! Used insert from postgresql dialect, when changing the DBMS, you will have to update this method
        """
        db_departments = [
            department_dto_to_db(department) for department in departments
        ]

        stmt = insert(Department).values(
            [
                {
                    "id": department.id,
                    "parent_id": department.parent_id,
                    "code": department.code,
                    "fullname": department.fullname,
                    "shortname": department.shortname,
                    "type": department.type,
                    "inn": department.inn,
                    "kpp": department.kpp,
                    "ogrn": department.ogrn,
                    "address": department.address,
                    "contacts": department.contacts,
                }
                for department in db_departments
            ],
        )

        stmt = stmt.on_conflict_do_update(
            index_elements=[Department.id],
            set_={
                "parent_id": stmt.excluded.parent_id,
                "code": stmt.excluded.code,
                "fullname": stmt.excluded.fullname,
                "shortname": stmt.excluded.shortname,
                "type": stmt.excluded.type,
                "inn": stmt.excluded.inn,
                "kpp": stmt.excluded.kpp,
                "ogrn": stmt.excluded.ogrn,
                "address": stmt.excluded.address,
                "contacts": stmt.excluded.contacts,
            },
        )

        await self.session.execute(stmt)
