from uuid import UUID

from pydantic import BaseModel


class PatientDTO(BaseModel):
    id: UUID
    snils: str
    last_name: str
    first_name: str
    middle_name: str
    gender: str
    birth_date: str
    documents: list[dict]
    address: list[dict]
    monitoring: list[dict] | None = None
    contacts: list[dict]
