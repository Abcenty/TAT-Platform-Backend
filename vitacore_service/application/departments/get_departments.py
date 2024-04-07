from vitacore_service.application.common.departments_gateway import (
    DepartmentReader,
    DepartmentSaver,
)
from vitacore_service.application.common.interactor import Interactor
from vitacore_service.application.common.uow import UoW
from vitacore_service.application.departments.converter import (
    department_dto_to_response,
)
from vitacore_service.application.departments.schemas import (
    DepartmentRead,
    GetDepartmentsRequest,
)
from vitacore_service.domain.services.departments import DepartmentsService


class GetDepartments(Interactor[GetDepartmentsRequest, DepartmentRead]):
    def __init__(
        self,
        http_departments_reader: DepartmentReader,
        db_departments_saver: DepartmentSaver,
        departments_service: DepartmentsService,
        uow: UoW,
    ):
        self.uow = uow
        self.db_departments_saver = db_departments_saver
        self.http_departments_reader = http_departments_reader
        self.departments_service = departments_service

    async def __call__(
        self,
        data: GetDepartmentsRequest = None,
    ) -> list[DepartmentRead]:
        departments = await self.http_departments_reader.get_all()

        departments = [
            self.departments_service.create(
                id=department.id,
                parent_id=department.parent_id,
                code=department.code,
                fullname=department.fullname,
                shortname=department.shortname,
                type=department.type,
                inn=department.inn,
                kpp=department.kpp,
                ogrn=department.ogrn,
                address=department.address,
                contacts=department.contacts,
            )
            for department in departments
        ]

        await self.db_departments_saver.bulk_save_with_update(departments)
        await self.uow.commit()

        return [department_dto_to_response(department) for department in departments]
