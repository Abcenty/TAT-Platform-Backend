from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Query, HTTPException

from vitacore_service.application.common.schemas import ErrorMessage
from vitacore_service.application.workers.schemas import GetWorkersRequest, WorkerRead
from vitacore_service.domain.exceptions.positions import PositionBadDepartmentError
from vitacore_service.domain.exceptions.vitacore import VitacoreError
from vitacore_service.infra.dependencies import ioc_dep

router = APIRouter()


@router.get(
    "/workers",
    response_model=list[WorkerRead],
    name="Получить сотрудников МО",
    responses={
        530: {
            "model": ErrorMessage,
            "description": "Something went wrong with VitaCore... Check detail",
        },
        400: {
            "model": ErrorMessage,
            "description": (
                "It is impossible to save the result because one of the organizations is "
                "not in the database. Try the /departments method first"
            ),
        },
    },
)
async def get_workers_by_department(
    ioc: ioc_dep,
    department_id: Annotated[
        UUID,
        Query(title="ID МО или филиала", description="ID МО или филиала"),
    ],
):
    """
    Возвращает список действующих сотрудников МО в разрезе филиалов.
    ID организации или филиала может быть получен методом `/departments`

    * Сохраняет результат в БД
    """
    async with ioc.get_workers_by_department() as get_workers:
        try:
            return await get_workers(
                GetWorkersRequest(department_id=department_id),
            )
        except VitacoreError as error:
            raise HTTPException(
                status_code=530,
                detail=str(error),
            )
        except PositionBadDepartmentError as error:
            raise HTTPException(
                status_code=400,
                detail=str(error),
            )
