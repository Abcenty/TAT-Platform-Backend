from fastapi import FastAPI

from tat_tsami_service.api.endpoints import statistics


def init_endpoints(app: FastAPI) -> None:
    app.include_router(
        router=statistics.router,
        tags=["statistics"],
    )
