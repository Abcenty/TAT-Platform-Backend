from fastapi import FastAPI
from grpclib.client import Channel

from gateway.settings import settings


async def init_product_service(app: FastAPI) -> None:
    """
    Инициализация микросервиса продуктов.

    :param app: Экземпляр приложения.
    """
    channel = Channel(
        host=settings.product_service_grpc_host,
        port=settings.product_service_grpc_port,
    )
    app.state.product_channel = channel


def shutdown_product_service(app: FastAPI) -> None:
    """
    Остановка микросервиса продуктов.

    :param app: Экземпляр приложения.
    """
    app.state.product_channel.close()