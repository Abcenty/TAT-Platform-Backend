from fastapi import APIRouter

from vitacore_service.infra.dependencies import ioc_dep
from vitacore_service.application.departments.schemas import DepartmentRead

router = APIRouter()


@router.get(
    "/departments",
    response_model=list[DepartmentRead],
    name="Получить МО и филиалы",
)
async def get_all_departments(ioc: ioc_dep):
    """
    Возвращает список всех медицинских организаций и филиалов из VitaCore

    * Результат сохраняется в БД
    """
    async with ioc.get_departments() as get_departments:
        return await get_departments()
