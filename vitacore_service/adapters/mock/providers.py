from vitacore_service.adapters.mock.departments.departments_gateway import (
    MockDepartmentsGateway,
)
from vitacore_service.adapters.mock.patients.patients_gateway import MockPatientsGateway
from vitacore_service.adapters.mock.workers.workers_gateway import MockWorkersGateway


def get_mock_departments_gateway():
    return MockDepartmentsGateway()


def get_mock_patients_gateway():
    return MockPatientsGateway()


def get_mock_workers_gateway():
    return MockWorkersGateway()
