from datetime import date
from uuid import UUID

from pydantic import BaseModel

from vitacore_service.application.positions.schemas import PositionRead


class GetWorkersRequest(BaseModel):
    department_id: UUID


class WorkerRead(BaseModel):
    id: UUID
    SNILS: str
    lastName: str
    firstName: str
    middleName: str = ""
    birthDate: date
    dateBegin: date | None = None
    dateEnd: date | None = None
    positions: list[PositionRead]
    contacts: list[dict]
