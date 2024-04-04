from aiohttp import ClientSession

from vitacore_service.adapters.http.departments.departments_converter import list_to_department_dto
from vitacore_service.application.common.departments_gateway import DepartmentReader
from vitacore_service.domain.models.departments import DepartmentDTO
from vitacore_service.infra.config import Settings


class HttpDepartmentsGateway(DepartmentReader):
    def __init__(self, session: ClientSession, settings: Settings):
        self.session = session
        self.vitacore_url = settings.vitacore_url

    async def get_all(self) -> list[DepartmentDTO]:
        url = self.vitacore_url + 'forTis/departments'

        async with self.session.get(url) as response:
            if not response.ok:
                raise Exception  # TODO: добавить исключение

            result = await response.json()

        return list_to_department_dto(result)
