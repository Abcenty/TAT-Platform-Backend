from aiohttp import ClientSession

from vitacore_service.adapters.http.departments.departments_gateway import (
    HttpDepartmentsGateway,
)
from vitacore_service.adapters.http.patients.patients_gateway import HttpPatientsGateway
from vitacore_service.adapters.http.workers.workers_gateway import HttpWorkersGateway
from vitacore_service.infra.config import Settings


def get_http_departments_gateway(
    session: ClientSession,
    settings: Settings,
) -> HttpDepartmentsGateway:
    return HttpDepartmentsGateway(session=session, settings=settings)


def get_http_patients_gateway(
    session: ClientSession,
    settings: Settings,
) -> HttpPatientsGateway:
    return HttpPatientsGateway(session=session, settings=settings)


def get_http_workers_gateway(
    session: ClientSession,
    settings: Settings,
) -> HttpWorkersGateway:
    return HttpWorkersGateway(session=session, settings=settings)
