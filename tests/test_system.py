from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_system():
    response = client.get("/system")
    assert response.status_code == 200

    data = response.json()
    assert "cpu_percent" in data
    assert "memory_percent" in data
    assert "disk_percent" in data
