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


class GetDepartments(Interactor[GetDepartmentsRequest, DepartmentRead]):
    def __init__(
        self,
        http_departments_reader: DepartmentReader,
        db_departments_saver: DepartmentSaver,
        uow: UoW,
    ):
        self.uow = uow
        self.db_departments_saver = db_departments_saver
        self.http_departments_reader = http_departments_reader

    async def __call__(
        self,
        data: GetDepartmentsRequest = None,
    ) -> list[DepartmentRead]:
        departments = await self.http_departments_reader.get_all()

        await self.db_departments_saver.bulk_save_with_update(departments)
        await self.uow.commit()

        return [department_dto_to_response(department) for department in departments]
