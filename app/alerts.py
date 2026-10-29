from fastapi import APIRouter
import psutil

from app.config import settings

router = APIRouter()


@router.get("/alerts")
def alerts():
    alert_list = []
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("C:\\").percent

    if cpu > settings.CPU_ALERT_THRESHOLD:
        alert_list.append(
            f"HIGH CPU USAGE ({cpu}%)"
        )

    if memory > settings.MEMORY_ALERT_THRESHOLD:
        alert_list.append(
            f"HIGH MEMORY USAGE ({memory}%)"
        )

    if disk > settings.DISK_ALERT_THRESHOLD:
        alert_list.append(
            f"HIGH DISK USAGE ({disk}%)"
        )

    if not alert_list:
        alert_list.append("SYSTEM HEALTHY")

    return {
        "cpu_threshold": settings.CPU_ALERT_THRESHOLD,
        "memory_threshold": settings.MEMORY_ALERT_THRESHOLD,
        "disk_threshold": settings.DISK_ALERT_THRESHOLD,
        "alerts": alert_list
    }
