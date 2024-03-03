import asyncio
import logging
import multiprocessing
import uvicorn
from api_gateway.settings import settings
from api_gateway.web.application import get_app

if not settings.reload:
    from api_gateway.gunicorn_runner import StandaloneApplication


def number_of_workers() -> int:
    return (multiprocessing.cpu_count() * 2) + 1


def main() -> None:
    app = get_app()

    """Entrypoint of the application."""
    if settings.reload:
        config = uvicorn.Config(
            app,
            host=settings.host,
            port=settings.port,
            log_level=logging.INFO,
        )

        server = uvicorn.Server(config)

        asyncio.run(server.serve())
    else:
        # We choose gunicorn only if reload
        # option is not used, because reload
        # feature doen't work with Uvicorn workers.
        options = {
            "bind": f"{settings.host}:{settings.port}",
            "preload_app": True,
            "workers": number_of_workers(),
            "worker_class": "uvicorn.workers.UvicornWorker",
        }

        StandaloneApplication(app, options).run()


if __name__ == "__main__":
    main()
