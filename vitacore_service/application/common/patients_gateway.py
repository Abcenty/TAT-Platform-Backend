from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from vitacore_service.domain.models.patients import PatientDTO


class PatientSaver(Protocol):
    @abstractmethod
    async def save_with_update(self, patient: PatientDTO) -> None:
        raise NotImplementedError

    @abstractmethod
    async def bulk_save_with_update(self, patients: list[PatientDTO]) -> None:
        raise NotImplementedError


class PatientReader(Protocol):
    @abstractmethod
    async def get(self, patient_id: UUID) -> PatientDTO:
        raise NotImplementedError

    @abstractmethod
    async def find(
        self,
        findstr: str | None,
        snils: str | None,
        docnum: str | None,
    ) -> list[PatientDTO]:
        raise NotImplementedError


class PatientUpdater(Protocol):
    pass
