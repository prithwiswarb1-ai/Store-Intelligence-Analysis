import json
import time
import random
import uuid
from datetime import datetime, timedelta
import requests

API_URL = "http://localhost:8000/events/ingest"

STORE_ID = "STORE_BLR_001"

CAMERAS = {
    "ENTRY": "CAM_ENTRY_01",
    "FLOOR": "CAM_FLOOR_01",
    "BILLING": "CAM_BILLING_01"
}

ZONES = [
    "SKINCARE",
    "MAKEUP",
    "FRAGRANCE",
    "HAIRCARE",
    "BILLING"
]

EVENT_TYPES = [
    "ENTRY",
    "ZONE_ENTER",
    "ZONE_DWELL",
    "BILLING_QUEUE_JOIN",
    "EXIT"
]


def generate_visitor_id():
    return f"VIS_{uuid.uuid4().hex[:6]}"


def create_event(
    visitor_id,
    event_type,
    zone_id=None,
    dwell_ms=0,
    queue_depth=None,
    session_seq=1
):

    camera_id = CAMERAS["FLOOR"]

    if event_type in ["ENTRY", "EXIT"]:
        camera_id = CAMERAS["ENTRY"]

    if event_type == "BILLING_QUEUE_JOIN":
        camera_id = CAMERAS["BILLING"]

    event = {
        "event_id": str(uuid.uuid4()),
        "store_id": STORE_ID,
        "camera_id": camera_id,
        "visitor_id": visitor_id,
        "event_type": event_type,
        "timestamp": datetime.utcnow().isoformat(),
        "zone_id": zone_id,
        "dwell_ms": dwell_ms,
        "is_staff": random.choice([False, False, False, True]),
        "confidence": round(random.uniform(0.80, 0.99), 2),
        "metadata": {
            "queue_depth": queue_depth,
            "sku_zone": zone_id,
            "session_seq": session_seq
        }
    }

    return event


def generate_session():

    visitor_id = generate_visitor_id()

    session_events = []

    seq = 1

    # ENTRY EVENT
    session_events.append(
        create_event(
            visitor_id=visitor_id,
            event_type="ENTRY",
            session_seq=seq
        )
    )

    seq += 1

    # RANDOM ZONE VISITS
    visited_zones = random.sample(ZONES[:-1], random.randint(1, 3))

    for zone in visited_zones:

        session_events.append(
            create_event(
                visitor_id=visitor_id,
                event_type="ZONE_ENTER",
                zone_id=zone,
                session_seq=seq
            )
        )

        seq += 1

        dwell_time = random.randint(10000, 90000)

        session_events.append(
            create_event(
                visitor_id=visitor_id,
                event_type="ZONE_DWELL",
                zone_id=zone,
                dwell_ms=dwell_time,
                session_seq=seq
            )
        )

        seq += 1

    # BILLING EVENT
    if random.random() > 0.3:

        session_events.append(
            create_event(
                visitor_id=visitor_id,
                event_type="BILLING_QUEUE_JOIN",
                zone_id="BILLING",
                queue_depth=random.randint(1, 8),
                session_seq=seq
            )
        )

        seq += 1

    # EXIT EVENT
    session_events.append(
        create_event(
            visitor_id=visitor_id,
            event_type="EXIT",
            session_seq=seq
        )
    )

    return session_events


def send_events(events):

    try:

        response = requests.post(
            API_URL,
            json=events,
            timeout=5
        )

        print(
            f"Sent {len(events)} events | "
            f"Status: {response.status_code}"
        )

        print(response.json())

    except Exception as e:

        print("ERROR:", str(e))


def save_events_to_jsonl(events, filename="data/generated_events.jsonl"):

    with open(filename, "a") as f:

        for event in events:
            f.write(json.dumps(event) + "\n")


def run_simulation():

    print("Starting Store Intelligence Event Simulation...")

    while True:

        session_events = generate_session()

        send_events(session_events)

        save_events_to_jsonl(session_events)

        print("=" * 50)

        time.sleep(random.randint(2, 5))


if __name__ == "__main__":
    run_simulation()