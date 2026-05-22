# PROMPT:
# Generate tests for metrics endpoint.
#
# CHANGES MADE:
# Added response structure validation.


from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_metrics_endpoint():

    response = client.get(
        "/stores/STORE_BLR_001/metrics"
    )

    assert response.status_code == 200

    data = response.json()

    assert "unique_visitors" in data
    assert "conversion_rate" in data