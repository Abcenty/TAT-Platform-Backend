from uuid import UUID

from pydantic import BaseModel


class GetPatientRequest(BaseModel):
    patient_id: UUID


class GetPatientResponse(BaseModel):
    id: UUID
    SNILS: str
    lastName: str
    firstName: str
    middleName: str
    gender: str
    birthDate: str
    documents: list[dict]
    address: list[dict]
    monitoring: list[dict] | None
    contacts: list[dict]
