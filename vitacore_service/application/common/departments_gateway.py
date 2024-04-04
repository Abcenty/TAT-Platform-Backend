from abc import abstractmethod
from typing import Protocol

from vitacore_service.domain.models.departments import DepartmentDTO


class DepartmentSaver(Protocol):
    @abstractmethod
    async def create(self, department: DepartmentDTO) -> None:
        raise NotImplementedError

    @abstractmethod
    async def create_bulk(self, departments: list[DepartmentDTO]) -> None:
        raise NotImplementedError


class DepartmentReader(Protocol):
    @abstractmethod
    async def get_all(self) -> list[DepartmentDTO]:
        raise NotImplementedError


class DepartmentUpdater(Protocol):
    @abstractmethod
    async def update(self, department: DepartmentDTO) -> None:
        raise NotImplementedError
