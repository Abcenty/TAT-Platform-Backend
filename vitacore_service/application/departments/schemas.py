from uuid import UUID

from pydantic import BaseModel, ConfigDict


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
    id: UUID
    parentId: UUID | None
    code: str
    fullname: str
    shortname: str
    type: str
    inn: str
    kpp: str
    ogrn: str
    address: list[dict]
    contacts: list[dict]


class GetDepartmentsRequest(TunedModel):
    pass
