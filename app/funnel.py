from sqlalchemy.orm import Session
from app.models import Event


def get_funnel(db: Session, store_id: str):

    events = db.query(Event).filter(
        Event.store_id == store_id,
        Event.is_staff == False
    ).all()

    visitors = set(e.visitor_id for e in events)

    zone_visitors = set(
        e.visitor_id
        for e in events
        if e.event_type == "ZONE_ENTER"
    )

    billing_visitors = set(
        e.visitor_id
        for e in events
        if e.event_type == "BILLING_QUEUE_JOIN"
    )

    return {
        "entry": len(visitors),
        "zone": len(zone_visitors),
        "billing": len(billing_visitors)
    }