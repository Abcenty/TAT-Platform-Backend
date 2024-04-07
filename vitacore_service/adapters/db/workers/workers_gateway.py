from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from vitacore_service.adapters.db.workers.workers_converter import worker_dto_to_db
from vitacore_service.application.common.workers_gateway import WorkerSaver
from vitacore_service.domain.models.workers import WorkerDTO
from vitacore_service.infra.db.models import Worker


class DBWorkersGateway(WorkerSaver):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def bulk_save_with_update(self, workers: list[WorkerDTO]) -> None:
        db_workers = [worker_dto_to_db(worker) for worker in workers]

        stmt = insert(Worker).values(
            [
                {
                    "id": worker.id,
                    "snils": worker.snils,
                    "last_name": worker.last_name,
                    "first_name": worker.first_name,
                    "middle_name": worker.middle_name,
                    "birth_date": worker.birth_date,
                    "date_begin": worker.date_begin,
                    "date_end": worker.date_end,
                    "contacts": worker.contacts,
                }
                for worker in db_workers
            ],
        )

        stmt = stmt.on_conflict_do_update(
            index_elements=[Worker.id],
            set_={
                "snils": stmt.excluded.snils,
                "last_name": stmt.excluded.last_name,
                "first_name": stmt.excluded.first_name,
                "middle_name": stmt.excluded.middle_name,
                "birth_date": stmt.excluded.birth_date,
                "date_begin": stmt.excluded.date_begin,
                "date_end": stmt.excluded.date_end,
                "contacts": stmt.excluded.contacts,
            },
        )

        await self.session.execute(stmt)
