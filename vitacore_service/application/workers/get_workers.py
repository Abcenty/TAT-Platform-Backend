from vitacore_service.application.common.interactor import Interactor
from vitacore_service.application.common.positions_gateway import PositionSaver
from vitacore_service.application.common.uow import UoW
from vitacore_service.application.common.workers_gateway import (
    WorkerReader,
    WorkerSaver,
)
from vitacore_service.application.workers.converter import worker_dto_to_response
from vitacore_service.application.workers.schemas import GetWorkersRequest, WorkerRead


class GetWorkers(Interactor[GetWorkersRequest, WorkerRead]):
    def __init__(
        self,
        http_workers_reader: WorkerReader,
        db_workers_saver: WorkerSaver,
        db_positions_saver: PositionSaver,
        uow: UoW,
    ):
        self.http_workers_reader = http_workers_reader
        self.db_workers_saver = db_workers_saver
        self.db_positions_saver = db_positions_saver
        self.uow = uow

    async def __call__(self, data: GetWorkersRequest) -> list[WorkerRead]:
        workers = await self.http_workers_reader.get_by_department(data.department_id)

        await self.db_workers_saver.save_bulk(workers)

        all_positions = list()
        for worker in workers:
            all_positions.extend(worker.positions)

        await self.db_positions_saver.save_bulk(all_positions)

        await self.uow.commit()

        return [worker_dto_to_response(worker) for worker in workers]
