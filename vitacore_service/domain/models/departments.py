from uuid import UUID

from pydantic import BaseModel


# class AddressDTO(BaseModel):
#     type: str
#     display: str
#     latitude: str | None
#     longitude: str | None
#
#
# class ContactDTO(BaseModel):
#     type: str
#     display: str


class DepartmentDTO(BaseModel):
    id: UUID
    parent_id: UUID | None
    code: str
    fullname: str
    shortname: str
    type: str
    inn: str
    kpp: str
    ogrn: str
    address: list[dict]
    contacts: list[dict]
