# PROMPT:
# Generate pytest test cases for event ingestion API.
#
# CHANGES MADE:
# Added duplicate event validation manually.


from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_ingest_events():

    payload = [
        {
            "event_id": "100",
            "store_id": "STORE_BLR_001",
            "camera_id": "CAM_ENTRY_01",
            "visitor_id": "VIS_100",
            "event_type": "ENTRY",
            "timestamp": "2026-03-03T14:00:00Z",
            "zone_id": None,
            "dwell_ms": 0,
            "is_staff": False,
            "confidence": 0.96,
            "metadata": {
                "queue_depth": None,
                "sku_zone": None,
                "session_seq": 1
            }
        }
    ]

    response = client.post(
        "/events/ingest",
        json=payload
    )

    assert response.status_code == 200