from vitacore_service.application.positions.converter import position_dto_to_response
from vitacore_service.application.workers.schemas import WorkerRead
from vitacore_service.domain.models.workers import WorkerDTO


def worker_dto_to_response(worker: WorkerDTO) -> WorkerRead:
    return WorkerRead(
        id=worker.id,
        SNILS=worker.snils,
        lastName=worker.last_name,
        firstName=worker.first_name,
        middleName=worker.middle_name,
        birthDate=worker.birth_date,
        dateBegin=worker.date_begin,
        dateEnd=worker.date_end,
        positions=[position_dto_to_response(position) for position in worker.positions],
        contacts=worker.contacts,
    )
