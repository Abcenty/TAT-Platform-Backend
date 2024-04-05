from vitacore_service.domain.models.departments import DepartmentDTO
from vitacore_service.infra.db.models import Department


def department_db_to_dto(department: Department) -> DepartmentDTO:
    return DepartmentDTO(
        id=department.id,
        parent_id=department.parent_id,
        code=department.code,
        fullname=department.fullname,
        shortname=department.shortname,
        type=department.type,
        inn=department.inn,
        kpp=department.kpp,
        ogrn=department.ogrn,
        address=department.address,
        contacts=department.contacts,
    )


def department_dto_to_db(department: DepartmentDTO) -> Department:
    return Department(
        id=department.id,
        parent_id=department.parent_id,
        code=department.code,
        fullname=department.fullname,
        shortname=department.shortname,
        type=department.type,
        inn=department.inn,
        kpp=department.kpp,
        ogrn=department.ogrn,
        address=department.address,
        contacts=department.contacts,
    )
