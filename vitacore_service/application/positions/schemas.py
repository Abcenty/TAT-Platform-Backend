from datetime import date
from typing import Any
from uuid import UUID

from pydantic import BaseModel


class PositionRead(BaseModel):
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
