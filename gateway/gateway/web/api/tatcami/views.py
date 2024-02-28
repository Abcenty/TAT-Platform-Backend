from fastapi import APIRouter, status
from web.exceptions import BadRequest, DetailedHTTPException, AbstractError
import logging

router = APIRouter()


@router.get(
    path="/ping",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Соединение со шлюзом для ТатЦАМИ установлено"},
        status.HTTP_400_BAD_REQUEST: {"model": BadRequest},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": DetailedHTTPException},
    },
)
async def ping():
    "Проверка соединения со шлюзом для ТатЦАМИ"
    try:
        logging.debug("Connection established")
        return "Соединение со шлюзом для ТатЦАМИ установлено"
    except AbstractError as error:
        if error.message == "BadRequest":
            raise BadRequest
        logging.error(f"Error while connecting to TatCAMI gateway ({error.status}: {error.message})")
        raise DetailedHTTPException()
    

