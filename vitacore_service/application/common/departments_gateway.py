from abc import abstractmethod
from typing import Protocol

from vitacore_service.domain.models.departments import DepartmentDTO


class DepartmentSaver(Protocol):
    @abstractmethod
    async def bulk_save_with_update(self, departments: list[DepartmentDTO]) -> None:
        raise NotImplementedError


class DepartmentReader(Protocol):
    @abstractmethod
    async def get_all(self) -> list[DepartmentDTO]:
        raise NotImplementedError


class DepartmentUpdater(Protocol):
    @abstractmethod
    async def update(self, department: DepartmentDTO) -> None:
        raise NotImplementedError
