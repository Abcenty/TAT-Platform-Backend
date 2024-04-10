from typing import Optional
from api_gateway import logging
from fastapi import APIRouter, status

from api_gateway.services.vitacore.lifetime import vitacore_get_session
from api_gateway.web.exceptions import AbstractError


router = APIRouter()

@router.get(
    path='/forTis/departments',
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"description": "..."}
    }
)
async def departments():
    """
    """
    try:
        return await vitacore_get_session('/forTis/departments')
    except AbstractError as error:
        logging.error(
            f"Error while authorization:({error.status}: {error.message})",
        )
        raise Exception()

@router.get(
    path='/forTis/workers',
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"description": "..."}
    }
)
async def workers(departmentid: str):
    """
    """
    try:
        return await vitacore_get_session('/forTis/workers', params={
            'departmentid': departmentid
        })
    except AbstractError as error:
        logging.error(
            f"Error while authorization:({error.status}: {error.message})",
        )
        raise Exception()

@router.get(
    path='/forTis/find_patients',
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"description": "..."}
    }
)
async def find_patients(findstr: Optional[str] = None, snils: Optional[str] = None, docnum: Optional[str] = None, lastName: Optional[str] = None, firstName: Optional[str] = None, middleName: Optional[str] = None, birthDate: Optional[str] = None):
    """
    """
    try:
        return await vitacore_get_session('/forTis/find_patients', params={
            'findstr': findstr,
            'snils': snils,
            'docnum': docnum,
            'lastName': lastName,
            'firstName': firstName,
            'middleName': middleName,
            'birthDate': birthDate
        })
    except AbstractError as error:
        logging.error(
            f"Error while authorization:({error.status}: {error.message})",
        )
        raise Exception()

@router.get(
    path='/forTis/patient',
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"description": "..."}
    }
)
async def patient(patid: str):
    """
    """
    try:
        return await vitacore_get_session('/forTis/patient', params={'patid': patid})
    except AbstractError as error:
        logging.error(
            f"Error while authorization:({error.status}: {error.message})",
        )
        raise Exception()
