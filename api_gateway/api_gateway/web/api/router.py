from fastapi import APIRouter
from api_gateway.web.api import (
    user_service,
    tatcami,
    vitacore
)

api_router = APIRouter()

api_router.include_router(user_service.router, prefix="/user_service", tags=["ТатЦАМИ"])
api_router.include_router(tatcami.router, prefix="/tatcami", tags=["ТатЦАМИ"])
api_router.include_router(vitacore.router, prefix="/vitacore", tags=["VitaCore"])
