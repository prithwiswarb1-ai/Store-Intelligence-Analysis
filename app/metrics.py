from sqlalchemy.orm import Session
from app.models import Event


def get_metrics(db: Session, store_id: str):

    events = db.query(Event).filter(
        Event.store_id == store_id,
        Event.is_staff == False
    ).all()

    unique_visitors = len(
        set(e.visitor_id for e in events)
    )

    billing_visitors = len(
        set(
            e.visitor_id
            for e in events
            if e.event_type == "BILLING_QUEUE_JOIN"
        )
    )

    conversion_rate = 0

    if unique_visitors > 0:
        conversion_rate = billing_visitors / unique_visitors

    avg_dwell = 0

    dwell_events = [
        e.dwell_ms
        for e in events
        if e.dwell_ms > 0
    ]

    if dwell_events:
        avg_dwell = sum(dwell_events) / len(dwell_events)

    return {
        "unique_visitors": unique_visitors,
        "conversion_rate": round(conversion_rate, 2),
        "avg_dwell_ms": avg_dwell
    }