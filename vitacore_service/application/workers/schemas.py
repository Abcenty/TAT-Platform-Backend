from datetime import date
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, Field

from vitacore_service.application.positions.schemas import PositionRead


class GetWorkersRequest(BaseModel):
    department_id: UUID


class WorkerRead(BaseModel):
    id: Annotated[UUID, Field(description="Идентификатор сотрудника")]
    SNILS: Annotated[str, Field(description="СНИЛС сотрудника")]
    lastName: Annotated[str, Field(description="Фамилия сотрудника")]
    firstName: Annotated[str, Field(description="Имя сотрудника")]
    middleName: Annotated[str, Field(description="Отчество сотрудника")] = ""
    birthDate: Annotated[date, Field(description="Дата рождения сотрудника")]
    dateBegin: Annotated[date | None, Field(description="Дата начала работы")] = None
    dateEnd: Annotated[date | None, Field(description="Дата окончания работы")] = None
    positions: Annotated[
        list[PositionRead],
        Field(description="Список должностей сотрудника"),
    ]
    contacts: Annotated[list[dict], Field(description="Список контактов сотрудника")]
