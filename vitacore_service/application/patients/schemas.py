from uuid import UUID

from pydantic import BaseModel


class GetPatientRequest(BaseModel):
    patient_id: UUID


class PatientRead(BaseModel):
    id: UUID
    SNILS: str | None
    lastName: str
    firstName: str
    middleName: str
    gender: str
    birthDate: str
    documents: list[dict]
    address: list[dict]
    monitoring: list[dict] | None
    contacts: list[dict] | None


class FindPatientsRequest(BaseModel):
    findstr: str | None
    snils: str | None
    docnum: str | None
