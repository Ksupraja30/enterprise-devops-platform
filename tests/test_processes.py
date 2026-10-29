from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_processes():
    response = client.get("/processes")
    assert response.status_code == 200

    data = response.json()
    assert "process_count" in data