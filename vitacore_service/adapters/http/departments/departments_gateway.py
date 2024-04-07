from json import JSONDecodeError

from aiohttp import ClientSession, ServerConnectionError

from vitacore_service.adapters.http.departments.departments_converter import (
    list_to_department_dto,
)
from vitacore_service.application.common.departments_gateway import DepartmentReader
from vitacore_service.domain.exceptions.vitacore import (
    VitacoreBadStatusError,
    VitacoreBadResponseError,
    VitacoreUnreachableError,
)
from vitacore_service.domain.models.departments import DepartmentDTO
from vitacore_service.infra.config import Settings


class HttpDepartmentsGateway(DepartmentReader):
    def __init__(self, session: ClientSession, settings: Settings):
        self.session = session
        self.vitacore_url = settings.vitacore_url

    async def get_all(self) -> list[DepartmentDTO]:
        url = self.vitacore_url + "forTis/departments"

        try:
            async with self.session.get(url) as response:
                if not response.ok:
                    raise VitacoreBadStatusError(f"Status code: {response.status}")

                try:
                    result = await response.json()
                except (JSONDecodeError, TypeError):
                    raise VitacoreBadResponseError(
                        f"Invalid JSON response: {response.text}",
                    )
        except ServerConnectionError:
            raise VitacoreUnreachableError()

        if not isinstance(result, list):
            raise VitacoreBadResponseError(f"JSON with error: {result}")

        return list_to_department_dto(result)
