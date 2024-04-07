from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, HTTPException, Query
from starlette import status

from vitacore_service.application.common.schemas import ErrorMessage
from vitacore_service.application.patients.schemas import (
    GetPatientRequest,
    FindPatientsRequest,
    PatientRead,
)
from vitacore_service.domain.exceptions.vitacore import VitacoreError
from vitacore_service.infra.dependencies import ioc_dep

router = APIRouter()


@router.get(
    "/patient",
    response_model=PatientRead,
    name="Получить пациента по ID",
    responses={
        530: {
            "model": ErrorMessage,
            "description": "Something went wrong with VitaCore... Check detail",
        },
    },
)
async def get_patient_by_id(
    ioc: ioc_dep,
    patient_id: Annotated[UUID, Query(title="ID пациента", description="ID пациента")],
):
    """
    Возвращает **полную** информацию о пациенте из VitaCore по его идентификатору (ID).
    Идентификатор нужного пациента можно узнать методом `/find_patients`

    * Результат сохраняется в БД
    """
    async with ioc.get_patient() as get_patient:
        try:
            return await get_patient(
                GetPatientRequest(patient_id=patient_id),
            )
        except VitacoreError as error:
            raise HTTPException(
                status_code=530,
                detail=str(error),
            )


@router.get(
    "/find_patients",
    response_model=list[PatientRead],
    name="Поиск пациентов",
    responses={
        530: {
            "model": ErrorMessage,
            "description": "Something went wrong with VitaCore... Check detail",
        },
    },
)
async def find_patients(
    ioc: ioc_dep,
    findstr: Annotated[
        str | None,
        Query(
            title="Поисковая строка",
            description=(
                "Может быть в виде:\n"
                '1. Первый буквы ФИО + дата рождения (например, "хтр11011987")\n'
                '2. Первые буквы ФИ + дата рождения (например, "ив20021990")'
            ),
        ),
    ] = None,
    snils: Annotated[
        str | None,
        Query(title="СНИЛС", description="Номер СНИЛС пациента"),
    ] = None,
    docnum: Annotated[
        str | None,
        Query(
            title="Номер документа",
            description="Номер паспорта или полиса ОМС пациента",
        ),
    ] = None,
):
    """
    Возвращает список пациентов из VitaCore подходящих под параметры поиска.
    Поиск пациента возможен по точному совпадению одного из параметров: findstr, snils, docnum.

    **Хотя бы один из параметров должен быть обязательно передан**

    * Сохраняет результат в БД
    * Не полностью соответствует этому же методу из VitaCora
    """
    if not any([findstr, snils, docnum]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="At least one of findstr or snils or docnum must be provided",
        )

    async with ioc.find_patients() as find_patients_func:
        try:
            return await find_patients_func(
                FindPatientsRequest(findstr=findstr, snils=snils, docnum=docnum),
            )
        except VitacoreError as error:
            raise HTTPException(
                status_code=530,
                detail=str(error),
            )
