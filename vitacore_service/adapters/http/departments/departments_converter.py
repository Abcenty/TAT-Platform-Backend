from vitacore_service.domain.models.departments import DepartmentDTO


def dict_to_department_dto(department_dict: dict) -> DepartmentDTO:
    return DepartmentDTO(
        id=department_dict.get("id"),
        parent_id=department_dict.get("parentId"),
        code=department_dict.get("code"),
        fullname=department_dict.get("fullname"),
        shortname=department_dict.get("shortname"),
        type=department_dict.get("type"),
        inn=department_dict.get("inn"),
        kpp=department_dict.get("kpp"),
        ogrn=department_dict.get("ogrn"),
        address=department_dict.get("address"),
        contacts=department_dict.get("contacts"),
    )


def list_to_department_dto(department_list: list[dict]) -> list[DepartmentDTO]:
    return [
        dict_to_department_dto(department_dict) for department_dict in department_list
    ]
