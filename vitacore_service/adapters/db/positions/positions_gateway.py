from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from vitacore_service.adapters.db.positions.positions_converter import (
    position_dto_to_db,
)
from vitacore_service.application.common.positions_gateway import PositionSaver
from vitacore_service.domain.models.positions import PositionDTO
from vitacore_service.infra.db.models import Position


class DBPositionsGateway(PositionSaver):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def bulk_save_with_update(self, positions: list[PositionDTO]) -> None:
        """
        Adds several positions to the database. When there is a conflict, an update occurs.

        !!! Used insert from postgresql dialect, when changing the DBMS, you will have to update this method
        """
        db_positions = [position_dto_to_db(position) for position in positions]

        stmt = insert(Position).values(
            [
                {
                    "id": position.id,
                    "date_begin": position.date_begin,
                    "department_id": position.department_id,
                    "department_name": position.department_name,
                    "position_name": position.position_name,
                    "position_rate": position.position_rate,
                    "position_fed_code": position.position_fed_code,
                    "position_reg_name": position.position_reg_name,
                    "position_speciality_code": position.position_speciality_code,
                    "position_speciality_name": position.position_speciality_name,
                    "worker_id": position.worker_id,
                }
                for position in db_positions
            ],
        )

        stmt = stmt.on_conflict_do_update(
            index_elements=[Position.id],
            set_={
                "date_begin": stmt.excluded.date_begin,
                "department_id": stmt.excluded.department_id,
                "department_name": stmt.excluded.department_name,
                "position_name": stmt.excluded.position_name,
                "position_rate": stmt.excluded.position_rate,
                "position_fed_code": stmt.excluded.position_fed_code,
                "position_reg_name": stmt.excluded.position_reg_name,
                "position_speciality_code": stmt.excluded.position_speciality_code,
                "position_speciality_name": stmt.excluded.position_speciality_name,
                "worker_id": stmt.excluded.worker_id,
            },
        )

        await self.session.execute(stmt)
