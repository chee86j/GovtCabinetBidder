import os

os.environ["APP_ENV"] = "test"

import pytest
from fastapi.testclient import TestClient

import app.main
from app.db.session import DatabaseConnectionError


@pytest.fixture
def client() -> TestClient:
    return TestClient(app.main.app)


def test_health_returns_expected_payload(client: TestClient) -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "government-cabinet-bid-agent-api",
    }


def test_database_health_returns_connected_when_check_succeeds(
    client: TestClient,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(app.main, "check_database_connection", lambda settings: None)

    response = client.get("/health/db")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "database": "connected",
    }


def test_database_health_returns_clear_error_when_check_fails(
    client: TestClient,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fail_database_check(settings: object) -> None:
        raise DatabaseConnectionError("Database connection failed: could not connect")

    monkeypatch.setattr(app.main, "check_database_connection", fail_database_check)

    response = client.get("/health/db")

    assert response.status_code == 503
    assert response.json() == {
        "status": "error",
        "database": "disconnected",
        "detail": "Database connection failed: could not connect",
    }
