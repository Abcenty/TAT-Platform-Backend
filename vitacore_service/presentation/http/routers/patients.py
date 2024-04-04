from uuid import UUID

from fastapi import APIRouter

from vitacore_service.application.patients.schemas import GetPatientRequest
from vitacore_service.infra.dependencies import ioc_dep

router = APIRouter()


@router.get('/patient')
async def get_patient_by_id(ioc: ioc_dep, patient_id: UUID):
    async with ioc.get_patient() as get_patient:
        return await get_patient(
            GetPatientRequest(patient_id=patient_id)
        )
