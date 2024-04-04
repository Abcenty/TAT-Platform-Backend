from fastapi import APIRouter

from .departments import router as departments_router
from .patients import router as patients_router

router = APIRouter()

router.include_router(departments_router)
router.include_router(patients_router)
