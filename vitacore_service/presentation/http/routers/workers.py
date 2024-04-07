from uuid import UUID

from fastapi import APIRouter

from vitacore_service.application.workers.schemas import GetWorkersRequest
from vitacore_service.infra.dependencies import ioc_dep

router = APIRouter()


@router.get("/workers")
async def get_workers_by_department(ioc: ioc_dep, department_id: UUID):
    async with ioc.get_workers_by_department() as get_workers:
        return await get_workers(
            GetWorkersRequest(department_id=department_id),
        )
