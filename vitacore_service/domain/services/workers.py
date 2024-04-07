from datetime import date
from uuid import UUID

from vitacore_service.domain.models.workers import WorkerDTO
from vitacore_service.domain.services.base import BaseService


class WorkersService(BaseService):
    @staticmethod
    def create(
        id: UUID,
        snils: str,
        last_name: str,
        first_name: str,
        birth_date: date,
        contacts: list[dict],
        date_begin: date | None = None,
        date_end: date | None = None,
        middle_name: str = "",
    ) -> WorkerDTO:
        return WorkerDTO(
            id=id,
            snils=snils,
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
            birth_date=birth_date,
            date_begin=date_begin,
            date_end=date_end,
            contacts=contacts,
        )
