from uuid import UUID

from vitacore_service.domain.models.positions import PositionDTO


def dict_to_position_dto(position_dict: dict, worker_id: UUID) -> PositionDTO:
    return PositionDTO(
        id=position_dict.get("id"),
        date_begin=position_dict.get("dateBegin"),
        department_id=position_dict.get("departmentId"),
        department_name=position_dict.get("departmentName"),
        position_name=position_dict.get("positionName"),
        position_rate=position_dict.get("positionRate"),
        position_fed_code=position_dict.get("positionFedCode"),
        position_reg_name=position_dict.get("positionRegName"),
        position_speciality_code=position_dict.get("positionSpecialityCode"),
        position_speciality_name=position_dict.get("positionSpecialityName"),
        worker_id=worker_id,
    )
