from abc import ABC, abstractmethod
from typing import AsyncContextManager

from vitacore_service.application.departments.get_departments import GetDepartments
from vitacore_service.application.patients.get_patient import GetPatient
from vitacore_service.application.workers.get_workers import GetWorkers


class InteractorFactory(ABC):
    @abstractmethod
    def get_departments(self) -> AsyncContextManager[GetDepartments]:
        raise NotImplementedError

    @abstractmethod
    def get_patient(self) -> AsyncContextManager[GetPatient]:
        raise NotImplementedError

    @abstractmethod
    def get_workers_by_department(self) -> AsyncContextManager[GetWorkers]:
        raise NotImplementedError
