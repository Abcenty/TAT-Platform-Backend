from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from domain.models.patients import PatientDTO


class PatientSaver(Protocol):
    @abstractmethod
    async def create(self, patient: PatientDTO):
        pass


class PatientReader(Protocol):
    @abstractmethod
    async def get(self, patient_id: UUID) -> PatientDTO:
        raise NotImplementedError


class PatientUpdater(Protocol):
    pass
