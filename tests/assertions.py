import requests

BASE_URL = "http://localhost:8000"


def test_health():

    response = requests.get(
        f"{BASE_URL}/health"
    )

    assert response.status_code == 200


def test_metrics():

    response = requests.get(
        f"{BASE_URL}/stores/STORE_BLR_001/metrics"
    )

    assert response.status_code == 200

    data = response.json()

    assert "unique_visitors" in data
    assert "conversion_rate" in data


def test_funnel():

    response = requests.get(
        f"{BASE_URL}/stores/STORE_BLR_001/funnel"
    )

    assert response.status_code == 200


def test_anomalies():

    response = requests.get(
        f"{BASE_URL}/stores/STORE_BLR_001/anomalies"
    )

    assert response.status_code == 200