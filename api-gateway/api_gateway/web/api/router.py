from fastapi import APIRouter
from api_gateway.web.api import (
    tatcami,
)

api_router = APIRouter()

api_router.include_router(tatcami.router, prefix="/tatcami", tags=["ТатЦАМИ"])
