from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_ok() -> None:
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_hello_default() -> None:
    r = client.get("/api/hello")
    body = r.json()
    assert r.status_code == 200
    assert body["message"] == "Hello Skilluv!"
    assert "server_time" in body


def test_hello_with_name() -> None:
    r = client.get("/api/hello", params={"name": "Ada"})
    assert r.json()["message"] == "Hello Ada!"


def test_hello_trims_and_falls_back() -> None:
    r = client.get("/api/hello", params={"name": "   "})
    assert r.json()["message"] == "Hello Skilluv!"
