from fastapi import APIRouter

from vitacore_service.infra.dependencies import ioc_dep
from vitacore_service.application.departments.schemas import DepartmentRead

router = APIRouter()


@router.get('/departments', response_model=list[DepartmentRead])
async def get_all_departments(ioc: ioc_dep):
    async with ioc.get_departments() as get_departments:
        return await get_departments()
