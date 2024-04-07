from vitacore_service.adapters.http.positions.positions_converter import (
    dict_to_position_dto,
)
from vitacore_service.domain.models.workers import WorkerDTO


def dict_to_worker_dto(worker_dict: dict) -> WorkerDTO:
    return WorkerDTO(
        id=worker_dict.get("id"),
        snils=worker_dict.get("snils"),
        last_name=worker_dict.get("lastName"),
        first_name=worker_dict.get("firstName"),
        middle_name=worker_dict.get("middleName"),
        birth_date=worker_dict.get("birthDate"),
        date_begin=worker_dict.get("dateBegin"),
        date_end=worker_dict.get("dateEnd"),
        positions=[
            dict_to_position_dto(position_dict, worker_id=worker_dict.get("id"))
            for position_dict in worker_dict.get("positions")
        ],
        contacts=worker_dict.get("contacts"),
    )
