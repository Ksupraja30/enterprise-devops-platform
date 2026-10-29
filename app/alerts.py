from fastapi import APIRouter
import psutil

router = APIRouter()

@router.get("/alerts")
def alerts():

    alert_list = []

    cpu = psutil.cpu_percent()

    memory = psutil.virtual_memory().percent

    disk = psutil.disk_usage("C:\\").percent

    if cpu > 80:
        alert_list.append("HIGH CPU USAGE")

    if memory > 80:
        alert_list.append("HIGH MEMORY USAGE")

    if disk > 80:
        alert_list.append("HIGH DISK USAGE")

    if not alert_list:
        alert_list.append("SYSTEM HEALTHY")

    return {
        "alerts": alert_list
    }