from uuid import UUID

from fastapi import APIRouter, HTTPException
from starlette import status

from vitacore_service.application.patients.schemas import (
    GetPatientRequest,
    FindPatientsRequest,
)
from vitacore_service.infra.dependencies import ioc_dep

router = APIRouter()


@router.get("/patient")
async def get_patient_by_id(ioc: ioc_dep, patient_id: UUID):
    async with ioc.get_patient() as get_patient:
        return await get_patient(
            GetPatientRequest(patient_id=patient_id),
        )


@router.get("/find_patients")
async def find_patients_handler(
    ioc: ioc_dep,
    findstr: str | None = None,
    snils: str | None = None,
    docnum: str | None = None,
):
    if not any([findstr, snils, docnum]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="At least one of findstr or snils or docnum must be provided",
        )

    async with ioc.find_patients() as find_patients:
        return await find_patients(
            FindPatientsRequest(findstr=findstr, snils=snils, docnum=docnum),
        )
