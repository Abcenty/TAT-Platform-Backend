from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class TunedModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


# class AddressRead(TunedModel):
#     type: str
#     display: str
#     latitude: str | None
#     longitude: str | None
#
#
# class ContactRead(TunedModel):
#     type: str
#     display: str


class DepartmentRead(TunedModel):
    id: Annotated[UUID, Field(description="Идентификатор МО")]
    parentId: Annotated[
        UUID | None,
        Field(description="Идентификатор вышестоящего подразделения"),
    ]
    code: Annotated[str, Field(description="Региональный код или код ТФОМС")]
    fullname: Annotated[str, Field(description="Полное наименование")]
    shortname: Annotated[str, Field(description="Краткое наименование")]
    type: Annotated[
        str,
        Field(
            description=(
                "Тип подразделения:"
                "* Для МО: «Юридический»"
                "* Для филиалов:"
                "Стационар / Поликлиника / ФАП / Амбулатория"
            ),
        ),
    ]
    inn: Annotated[str, Field(description="ИНН")]
    kpp: Annotated[str, Field(description="КПП")]
    ogrn: Annotated[str, Field(description="ОГРН")]
    address: Annotated[list[dict], Field(description="Список адресов")]
    contacts: Annotated[list[dict], Field(description="Список контактов")]


class GetDepartmentsRequest(TunedModel):
    pass
