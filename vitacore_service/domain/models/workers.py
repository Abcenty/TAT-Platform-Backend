from datetime import date
from uuid import UUID

from pydantic import BaseModel

from vitacore_service.domain.models.positions import PositionDTO


# class ContactDTO(BaseModel):
#     type: str
#     display: str


class WorkerDTO(BaseModel):
    id: UUID
    snils: str
    last_name: str
    first_name: str
    middle_name: str = ""
    birth_date: date
    date_begin: date | None = None
    date_end: date | None = None
    positions: list[PositionDTO]
    contacts: list[dict]
