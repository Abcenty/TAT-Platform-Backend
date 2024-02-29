from typing import Any, Union, Dict

from aiohttp import ClientResponseError, ClientConnectionError
from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.status import (
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_503_SERVICE_UNAVAILABLE,
)


def init_exceptions(app: FastAPI) -> None:
    app.add_exception_handler(
        ClientConnectionError,
        client_connection_error_handler,  # noqa
    )
    app.add_exception_handler(
        ClientResponseError,
        client_response_error_handler,  # noqa
    )

    app.add_exception_handler(Exception, exception_handler)


def client_connection_error_handler(_, err: ClientConnectionError) -> JSONResponse:
    return handle_error(detail=str(err), status_code=HTTP_503_SERVICE_UNAVAILABLE)


def client_response_error_handler(_, err: ClientResponseError) -> JSONResponse:
    return handle_error(detail=err.message, status_code=err.status)


def exception_handler(_, err: Exception) -> JSONResponse:
    return JSONResponse(
        {"detail": "Something went wrong"},
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
    )


def handle_error(
    detail: Union[Dict[str, Any], str],
    status_code: int,
) -> JSONResponse:
    return JSONResponse({"detail": detail}, status_code=status_code)
