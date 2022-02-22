from fastapi.testclient import TestClient

from config.routes import app

client = TestClient(app)


def test_health_route_sucessfuly():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_health_route_failure():
    response = client.get("/foobar")
    assert response.status_code == 400


def test_with_wrong_test():
    response = client.get("/foobar")
    assert response.status_code == 200
