from fastapi import APIRouter
import psutil
import socket
import platform

router = APIRouter()

@router.get("/system")
def system_info():

    return {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("C:\\").percent
    }