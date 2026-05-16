from __future__ import annotations

from typing import Optional

import pytest
from pydantic import ValidationError

from app.config import get_settings


@pytest.mark.parametrize(
    ("env_value", "database_url", "cors_origins"),
    [
        ("test", None, ""),
        ("development", "postgresql://user:pass@localhost:5432/app", "http://localhost:3000, http://127.0.0.1:3000"),
    ],
)
def test_settings_load_from_environment(
    monkeypatch: pytest.MonkeyPatch,
    env_value: str,
    database_url: Optional[str],
    cors_origins: str,
) -> None:
    monkeypatch.setenv("APP_ENV", env_value)
    if database_url is None:
        monkeypatch.delenv("DATABASE_URL", raising=False)
    else:
        monkeypatch.setenv("DATABASE_URL", database_url)
    monkeypatch.setenv("CORS_ORIGINS", cors_origins)

    settings = get_settings()

    assert settings.app_env == env_value
    assert settings.database_url == database_url
    if cors_origins:
        assert settings.cors_origin_list() == [
            "http://localhost:3000",
            "http://127.0.0.1:3000",
        ]
    else:
        assert settings.cors_origin_list() == []


def test_missing_database_url_fails_outside_test_mode(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("APP_ENV", "development")
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.delenv("CORS_ORIGINS", raising=False)

    with pytest.raises(ValidationError, match="DATABASE_URL is required"):
        get_settings()
