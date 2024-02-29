from pydantic.dataclasses import dataclass

from gateway.web.exceptions import DetailedHTTPException


@dataclass
class GetGeneralStatisticsError(DetailedHTTPException):
    detail: str = "Ошибка при получении общей статистики с ТатЦАМи"


@dataclass
class GetStatisticsOnOrganizationsError(DetailedHTTPException):
    detail: str = "Ошибка при получении статистики по организациям с ТатЦАМи"


@dataclass
class InvalidOrganizationIdError(DetailedHTTPException):
    detail: str = "Ошибка при получении id организации ТатЦАМи"


@dataclass
class GetDevicesOnOrganizationsError(DetailedHTTPException):
    detail: str = "Ошибка при получении устройств организации с ТатЦАМи"
