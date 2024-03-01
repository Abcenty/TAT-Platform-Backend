from pydantic.dataclasses import dataclass

from gateway.web.exceptions import DetailedHTTPException


@dataclass
class AuthorizationError(DetailedHTTPException):
    detail: str = "Ошибка при получении токена авторизации"
