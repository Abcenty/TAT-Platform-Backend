from fastapi import APIRouter, HTTPException

from vitacore_service.application.common.schemas import ErrorMessage
from vitacore_service.domain.exceptions.vitacore import VitacoreError
from vitacore_service.infra.dependencies import ioc_dep
from vitacore_service.application.departments.schemas import DepartmentRead

router = APIRouter()


@router.get(
    "/departments",
    response_model=list[DepartmentRead],
    name="Получить МО и филиалы",
    responses={
        530: {
            "model": ErrorMessage,
            "description": "Something went wrong with VitaCore... Check detail",
        },
    },
)
async def get_all_departments(ioc: ioc_dep):
    """
    Возвращает список всех медицинских организаций и филиалов из VitaCore

    * Результат сохраняется в БД
    """
    async with ioc.get_departments() as get_departments:
        try:
            return await get_departments()
        except VitacoreError as error:
            raise HTTPException(
                status_code=530,
                detail=str(error),
            )
