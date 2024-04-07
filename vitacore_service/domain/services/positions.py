from datetime import date
from typing import Any
from uuid import UUID

from vitacore_service.domain.models.positions import PositionDTO
from vitacore_service.domain.services.base import BaseService


class PositionsService(BaseService):
    @staticmethod
    def create(
        id: UUID,
        worker_id: UUID,
        date_begin: date,
        department_id: UUID,
        department_name: str,
        position_name: str,
        position_fed_code: str,
        position_reg_name: str | None,
        position_speciality_code: str | None = None,
        position_speciality_name: str | None = None,
        position_rate: Any = None,
    ) -> PositionDTO:
        return PositionDTO(
            id=id,
            worker_id=worker_id,
            date_begin=date_begin,
            department_id=department_id,
            department_name=department_name,
            position_name=position_name,
            position_rate=position_rate,
            position_fed_code=position_fed_code,
            position_reg_name=position_reg_name,
            position_speciality_code=position_speciality_code,
            position_speciality_name=position_speciality_name,
        )
