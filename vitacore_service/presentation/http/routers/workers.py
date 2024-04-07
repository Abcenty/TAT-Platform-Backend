from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Query

from vitacore_service.application.workers.schemas import GetWorkersRequest, WorkerRead
from vitacore_service.infra.dependencies import ioc_dep

router = APIRouter()


@router.get("/workers", response_model=list[WorkerRead], name="Получить сотрудников МО")
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
        return await get_workers(
            GetWorkersRequest(department_id=department_id),
        )
