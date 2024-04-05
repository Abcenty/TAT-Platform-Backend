from vitacore_service.application.departments.schemas import DepartmentRead
from vitacore_service.domain.models.departments import DepartmentDTO


def department_dto_to_response(department: DepartmentDTO) -> DepartmentRead:
    return DepartmentRead(
        id=department.id,
        parentId=department.parent_id,
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
