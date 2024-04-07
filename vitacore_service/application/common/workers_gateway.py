from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from vitacore_service.domain.models.workers import WorkerDTO


class WorkerSaver(Protocol):
    @abstractmethod
    async def bulk_save_with_update(self, workers: list[WorkerDTO]) -> None:
        raise NotImplementedError


class WorkerReader(Protocol):
    @abstractmethod
    async def get_by_department(self, department_id: UUID) -> list[WorkerDTO]:
        raise NotImplementedError


class WorkerUpdater(Protocol):
    pass
