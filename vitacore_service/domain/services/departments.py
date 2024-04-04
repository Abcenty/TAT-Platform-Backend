from uuid import UUID

from vitacore_service.domain.models.departments import DepartmentDTO
from vitacore_service.domain.services.base import BaseService


class DepartmentsService(BaseService):
    @staticmethod
    def create(
            id: UUID,
            parent_id: UUID | None,
            code: str,
            fullname: str,
            shortname: str,
            type: str,
            inn: str,
            kpp: str,
            ogrn: str,
            address: list[dict],
            contacts: list[dict]
    ) -> DepartmentDTO:
        return DepartmentDTO(
            id=id,
            parent_id=parent_id,
            code=code,
            fullname=fullname,
            shortname=shortname,
            type=type,
            inn=inn,
            kpp=kpp,
            ogrn=ogrn,
            address=address,
            contacts=contacts
        )
