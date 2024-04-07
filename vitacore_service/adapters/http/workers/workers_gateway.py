from uuid import UUID

from aiohttp import ClientSession

from vitacore_service.adapters.http.workers.workers_converter import dict_to_worker_dto
from vitacore_service.application.common.workers_gateway import WorkerReader
from vitacore_service.domain.models.workers import WorkerDTO
from vitacore_service.infra.config import Settings


class HttpWorkersGateway(WorkerReader):
    def __init__(self, session: ClientSession, settings: Settings):
        self.session = session
        self.vitacore_url = settings.vitacore_url

    async def get_by_department(self, department_id: UUID) -> list[WorkerDTO]:
        url = self.vitacore_url + f"/workers?departmentId={department_id}"

        async with self.session.get(url) as response:
            if not response.ok:
                raise Exception

            result = await response.json()

        return [dict_to_worker_dto(worker_dict) for worker_dict in result]
