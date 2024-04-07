from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, Field


class GetPatientRequest(BaseModel):
    patient_id: UUID


class PatientRead(BaseModel):
    id: Annotated[UUID, Field(description="Идентификатор пациента")]
    SNILS: Annotated[str | None, Field(description="СНИЛС пациента")]
    lastName: Annotated[str, Field(description="Фамилия пациента")]
    firstName: Annotated[str, Field(description="Имя пациента")]
    middleName: Annotated[str, Field(description="Отчество пациента")]
    gender: Annotated[str, Field(description="Пол")]
    birthDate: Annotated[str, Field(description="Дата рождения")]
    documents: Annotated[list[dict], Field(description="Список документов")]
    address: Annotated[list[dict], Field(description="Список адресов")]
    monitoring: Annotated[list[dict] | None, Field(description="Список диагнозов")]
    contacts: Annotated[list[dict] | None, Field(description="Список контактов")]


class FindPatientsRequest(BaseModel):
    findstr: str | None
    snils: str | None
    docnum: str | None
