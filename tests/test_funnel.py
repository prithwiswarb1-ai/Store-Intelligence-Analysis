# PROMPT:
# Generate tests for funnel analytics endpoint.
#
# CHANGES MADE:
# Added funnel stage validation.


from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_funnel_endpoint():

    response = client.get(
        "/stores/STORE_BLR_001/funnel"
    )

    assert response.status_code == 200

    data = response.json()

    assert "entry" in data
    assert "zone" in data
    assert "billing" in data