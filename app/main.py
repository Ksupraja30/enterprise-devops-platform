from fastapi import FastAPI

from prometheus_fastapi_instrumentator import Instrumentator

from app.health import router as health_router
from app.system import router as system_router
from app.processes import router as process_router
from app.alerts import router as alerts_router

app = FastAPI(
    title="Enterprise Infrastructure Monitoring Platform",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(system_router)
app.include_router(process_router)
app.include_router(alerts_router)

Instrumentator().instrument(app).expose(app)