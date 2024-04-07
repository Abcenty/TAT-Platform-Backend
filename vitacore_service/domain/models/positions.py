from datetime import date
from typing import Any
from uuid import UUID

from pydantic import BaseModel


class PositionDTO(BaseModel):
    id: UUID
    date_begin: date
    department_id: UUID
    department_name: str
    position_name: str
    position_rate: Any = None
    position_fed_code: str
    position_reg_name: str | None
    position_speciality_code: str | None = None
    position_speciality_name: str | None = None

    worker_id: UUID
