from fastapi import APIRouter
from app.logger import logger

router = APIRouter()

@router.get("/health")
def health():

    logger.info("Health endpoint invoked")

    return {
        "status": "healthy"
    }