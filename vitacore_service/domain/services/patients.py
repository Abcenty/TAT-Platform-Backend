from uuid import UUID

from domain.models.patients import PatientDTO
from domain.services.base import BaseService


class PatientsService(BaseService):
    @staticmethod
    def create(
            id: UUID,
            snils: str,
            last_name: str,
            first_name: str,
            middle_name: str,
            gender: str,
            birth_date: str,
            documents: list[dict],
            address: list[dict],
            contacts: list[dict],
            monitoring: list[dict] | None = None
    ):
        return PatientDTO(
            id=id,
            snils=snils,
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
            gender=gender,
            birth_date=birth_date,
            documents=documents,
            address=address,
            monitoring=monitoring,
            contacts=contacts
        )
