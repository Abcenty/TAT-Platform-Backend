import asyncio
import logging
import multiprocessing
import os
from sys import platform

import uvicorn

from tat_tsami_service.api.setup import register_app
from tat_tsami_service.settings.environments.base import AppEnvTypes
from tat_tsami_service.settings.main import get_app_settings


def number_of_workers() -> int:
    return (multiprocessing.cpu_count() * 2) + 1


def run_application() -> None:
    logging.getLogger("passlib").setLevel(logging.ERROR)
    settings = get_app_settings(
        app_env=AppEnvTypes.prod if os.getenv("IS_PRODUCTION") else AppEnvTypes.dev
    )
    app = register_app(settings=settings)

    if platform == "win32":
        config = uvicorn.Config(
            app,
            host=settings.server_host,
            port=settings.server_port,
            log_level=logging.INFO
        )

        server = uvicorn.Server(config)

        asyncio.run(server.serve())
    else:
        from tat_tsami_service.api.application import StandaloneApplication

        options = {
            "bind": f"{settings.server_host}:{settings.server_port}",
            "preload_app": True,
            "workers": number_of_workers(),
            "worker_class": "uvicorn.workers.UvicornWorker"
        }
        server = StandaloneApplication(app, options)
        server.run()


if __name__ == "__main__":
    run_application()
