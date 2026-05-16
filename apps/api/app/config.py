from __future__ import annotations

from typing import List, Optional

from pydantic import Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "government-cabinet-bid-agent-api"
    app_env: str = Field(default="development", alias="APP_ENV")
    database_url: Optional[str] = Field(default=None, alias="DATABASE_URL")
    cors_origins: str = Field(default="", alias="CORS_ORIGINS")

    @model_validator(mode="after")
    def validate_database_url(self) -> Settings:
        if self.app_env != "test" and not self.database_url:
            msg = "DATABASE_URL is required unless APP_ENV is set to 'test'."
            raise ValueError(msg)
        return self

    def cors_origin_list(self) -> List[str]:
        return [
            origin.strip()
            for origin in self.cors_origins.split(",")
            if origin.strip()
        ]


def get_settings() -> Settings:
    return Settings()
