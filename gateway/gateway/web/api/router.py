from fastapi import APIRouter
from gateway.web.api import (
    user_service,
    tatcami,
)

api_router = APIRouter()

api_router.include_router(user_service.router, prefix="/user_service", tags=["ТатЦАМИ"])
api_router.include_router(tatcami.router, prefix="/tatcami", tags=["ТатЦАМИ"])
