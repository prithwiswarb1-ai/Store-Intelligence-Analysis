from sqlalchemy.orm import Session
from app.models import Event


def get_anomalies(db: Session, store_id: str):

    events = db.query(Event).filter(
        Event.store_id == store_id
    ).all()

    anomalies = []

    queue_events = [
        e for e in events
        if e.event_type == "BILLING_QUEUE_JOIN"
    ]

    if len(queue_events) > 5:
        anomalies.append({
            "type": "QUEUE_SPIKE",
            "severity": "WARN",
            "suggested_action": "Open additional billing counters"
        })

    return anomalies