from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_alerts():
    response = client.get("/alerts")
    assert response.status_code == 200

    data = response.json()
    assert "alerts" in data