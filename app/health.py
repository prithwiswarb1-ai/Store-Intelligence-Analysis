from datetime import datetime


def health_status():

    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }