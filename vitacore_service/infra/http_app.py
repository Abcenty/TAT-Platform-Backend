import asyncio
import logging
import multiprocessing
from sys import platform

import uvicorn
from fastapi import FastAPI

from vitacore_service.infra.config import get_settings
from vitacore_service.presentation.http.routers import router


def number_of_workers() -> int:
    return (multiprocessing.cpu_count() * 2) + 1


def init_app() -> FastAPI:
    app = FastAPI(
        title="Vitacore Service",
    )

    app.include_router(router, prefix="/forTis")

    return app


def main():
    settings = get_settings()

    app = init_app()

    if platform == "win32":
        config = uvicorn.Config(
            app,
            host=settings.service_host,
            port=settings.service_port,
            log_level=logging.INFO,
        )

        server = uvicorn.Server(config)

        asyncio.run(server.serve())
    else:
        from vitacore_service.infra.gunicorn_runner import GunicornApplication

        options = {
            "bind": f"{settings.service_host}:{settings.service_port}",
            "preload_app": True,
            "workers": number_of_workers(),
            "worker_class": "uvicorn.workers.UvicornWorker",
        }
        server = GunicornApplication(app, options)
        server.run()


if __name__ == "__main__":
    main()
