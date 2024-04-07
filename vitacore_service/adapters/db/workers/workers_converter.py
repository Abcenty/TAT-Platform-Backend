from vitacore_service.domain.models.workers import WorkerDTO
from vitacore_service.infra.db.models import Worker


def worker_dto_to_db(worker: WorkerDTO) -> Worker:
    return Worker(
        id=worker.id,
        snils=worker.snils,
        last_name=worker.last_name,
        first_name=worker.first_name,
        middle_name=worker.middle_name,
        birth_date=worker.birth_date,
        date_begin=worker.date_begin,
        date_end=worker.date_end,
        contacts=worker.contacts,
    )


def worker_db_to_dto(worker: Worker) -> WorkerDTO:
    """
    The worker needs to have the positions attribute available
    """
    return WorkerDTO(
        id=worker.id,
        snils=worker.snils,
        last_name=worker.last_name,
        first_name=worker.first_name,
        middle_name=worker.middle_name,
        birth_date=worker.birth_date,
        date_begin=worker.date_begin,
        date_end=worker.date_end,
        positions=worker.positions,
        contacts=worker.contacts,
    )
