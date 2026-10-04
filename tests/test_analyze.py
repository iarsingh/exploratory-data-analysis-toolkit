from fastapi.testclient import TestClient
from eda.main import app

client = TestClient(app)


def test_summary():
    payload = client.post("/analyze", json={"rows": [{'cohort': 'a', 'value': 10}, {'cohort': 'a', 'value': 30}, {'cohort': 'b', 'value': 20}]}).json()
    assert payload["mean"] == 20.0
    assert payload["by_cohort"]["a"]


def test_empty_is_refused():
    assert client.post("/analyze", json={"rows": []}).status_code == 422
