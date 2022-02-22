from fastapi.testclient import TestClient

from config.routes import app

client = TestClient(app)


def test_health_route_sucessfuly():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_health_not_found():
    response = client.get("/foobar")
    assert response.status_code == 404
