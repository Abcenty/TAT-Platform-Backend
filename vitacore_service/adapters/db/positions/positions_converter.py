from vitacore_service.domain.models.positions import PositionDTO
from vitacore_service.infra.db.models import Position


def position_dto_to_db(position: PositionDTO) -> Position:
    return Position(
        id=position.id,
        date_begin=position.date_begin,
        department_id=position.department_id,
        department_name=position.department_name,
        position_name=position.position_name,
        position_rate=position.position_rate,
        position_fed_code=position.position_fed_code,
        position_reg_name=position.position_reg_name,
        position_speciality_code=position.position_speciality_code,
        position_speciality_name=position.position_speciality_name,
        worker_id=position.worker_id,
    )


def position_db_to_dto(position: Position) -> PositionDTO:
    return PositionDTO(
        id=position.id,
        date_begin=position.date_begin,
        department_id=position.department_id,
        department_name=position.department_name,
        position_name=position.position_name,
        position_rate=position.position_rate,
        position_fed_code=position.position_fed_code,
        position_reg_name=position.position_reg_name,
        position_speciality_code=position.position_speciality_code,
        position_speciality_name=position.position_speciality_name,
        worker_id=position.worker_id,
    )
