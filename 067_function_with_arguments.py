import os
import shutil

def check_disk_usage(threshold_percent):
    """Monitors root disk space and flags an alert if usage exceeds the threshold."""
    total, used, free = shutil.disk_usage("/")
    usage_pct = (used / total) * 100

    if usage_pct > threshold_percent:
        return f"ALERT: High disk usage detected at {usage_pct:.2f}%"

    return f"OK: Disk usage is normal at {usage_pct:.2f}%"


# Example execution by the administrator
print(check_disk_usage(threshold_percent=85))
