from json import JSONDecodeError
from uuid import UUID

from aiohttp import ClientSession, ServerConnectionError

from vitacore_service.adapters.http.workers.workers_converter import dict_to_worker_dto
from vitacore_service.application.common.workers_gateway import WorkerReader
from vitacore_service.domain.exceptions.vitacore import (
    VitacoreBadStatusError,
    VitacoreBadResponseError,
    VitacoreUnreachableError,
)
from vitacore_service.domain.models.workers import WorkerDTO
from vitacore_service.infra.config import Settings


class HttpWorkersGateway(WorkerReader):
    def __init__(self, session: ClientSession, settings: Settings):
        self.session = session
        self.vitacore_url = settings.vitacore_url

    async def get_by_department(self, department_id: UUID) -> list[WorkerDTO]:
        url = self.vitacore_url + f"/workers?departmentId={department_id}"

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
            # TODO: find out in what form VitaCore returns errors in order to process them
            raise VitacoreBadResponseError(f"JSON with error: {result}")

        return [dict_to_worker_dto(worker_dict) for worker_dict in result]
