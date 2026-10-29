from fastapi import APIRouter
import psutil

router = APIRouter()

@router.get("/processes")
def process_info():

    return {
        "process_count": len(psutil.pids())
    }