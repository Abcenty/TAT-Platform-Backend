from vitacore_service.application.positions.schemas import PositionRead
from vitacore_service.domain.models.positions import PositionDTO


def position_dto_to_response(position: PositionDTO) -> PositionRead:
    return PositionRead(
        id=position.id,
        dateBegin=position.date_begin,
        departmentId=position.department_id,
        departmentName=position.department_name,
        positionName=position.position_name,
        positionRate=position.position_rate,
        positionFedCode=position.position_fed_code,
        positionRegName=position.position_reg_name,
        positionSpecialityCode=position.position_speciality_code,
        positionSpecialityName=position.position_speciality_name,
    )
