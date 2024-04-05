from datetime import date
from typing import Any
from uuid import UUID

from pydantic import BaseModel


class PositionDTO(BaseModel):
    id: UUID
    dateBegin: date
    departmentId: UUID
    departmentName: str
    positionName: str
    positionRate: Any = None
    positionFedCode: str
    positionRegName: str | None
    positionSpecialityCode: str | None = None
    positionSpecialityName: str | None = None


class ContactDTO(BaseModel):
    type: str
    display: str


class WorkerDTO(BaseModel):
    id: UUID
    SNILS: str
    lastName: str
    firstName: str
    middleName: str = ""
    birthDate: date
    dateBegin: date
    dateEnd: date
    positions: list[PositionDTO]
    contacts: list[ContactDTO]

