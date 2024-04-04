from fastapi import APIRouter

from .departments import router as departments_router

router = APIRouter()

router.include_router(departments_router)
