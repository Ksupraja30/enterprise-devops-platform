import os
class Settings:
    APP_NAME = "Enterprise Infrastructure Monitoring Platform"
    VERSION = "1.0.0"

    CPU_ALERT_THRESHOLD = int(
        os.getenv("CPU_ALERT_THRESHOLD", 85)
    )

    MEMORY_ALERT_THRESHOLD = int(
        os.getenv("MEMORY_ALERT_THRESHOLD", 85)
    )

    DISK_ALERT_THRESHOLD = int(
        os.getenv("DISK_ALERT_THRESHOLD", 85)
    )

settings = Settings()
