from fastapi import HTTPException, status
from pydantic.dataclasses import dataclass
from typing import Optional, Any
from .exception_status import Status


class AbstractError(Exception):
    def __init__(
        self,
        status: Status,
        message: Optional[str] = None,
        details: Any = None,
    ) -> None:
        super().__init__(status, message, details)
        self.status = status
        #: Error message
        self.message = message
        #: Error details
        self.details = details


@dataclass
class DetailedHTTPException(HTTPException):
    """Детальное исключение."""

    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail: str = "Серверная ошибка"


@dataclass
class Forbidden(DetailedHTTPException):
    """Недостаточно прав."""

    status_code: int = status.HTTP_403_FORBIDDEN
    detail: str = "Недостаточно прав"


@dataclass
class BadRequest(DetailedHTTPException):
    """Неверный запрос."""

    status_code: int = status.HTTP_400_BAD_REQUEST
    detail: str = "Неверный запрос"


@dataclass
class Unauthorized(DetailedHTTPException):
    """Не авторизован."""

    status_code: int = status.HTTP_401_UNAUTHORIZED
    detail: str = "Не авторизован"


@dataclass
class NotFound(DetailedHTTPException):
    """Не найдено."""

    status_code: int = status.HTTP_404_NOT_FOUND
    detail: str = "Не найдено"
