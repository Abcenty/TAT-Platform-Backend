from abc import ABC, abstractmethod
from typing import AsyncContextManager

from vitacore_service.application.departments.get_departments import GetDepartments


class InteractorFactory(ABC):
    @abstractmethod
    def get_departments(self) -> AsyncContextManager[GetDepartments]:
        raise NotImplementedError
