from aiohttp import ClientSession

from vitacore_service.adapters.http.departments.departments_gateway import HttpDepartmentsGateway
from vitacore_service.infra.config import Settings


def get_http_departments_gateway(session: ClientSession, settings: Settings) -> HttpDepartmentsGateway:
    return HttpDepartmentsGateway(session=session, settings=settings)