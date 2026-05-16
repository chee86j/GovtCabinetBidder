from __future__ import annotations

from typing import Callable

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from app.config import Settings


class DatabaseConnectionError(RuntimeError):
    """Raised when the application cannot connect to the configured database."""


def create_database_engine(database_url: str) -> Engine:
    return create_engine(database_url, pool_pre_ping=True)


def create_session_factory(engine: Engine) -> sessionmaker:
    return sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_session_factory(settings: Settings) -> sessionmaker:
    if not settings.database_url:
        msg = "DATABASE_URL is not configured."
        raise DatabaseConnectionError(msg)
    engine = create_database_engine(settings.database_url)
    return create_session_factory(engine)


def check_database_connection(
    settings: Settings,
    engine_factory: Callable[[str], Engine] = create_database_engine,
) -> None:
    if not settings.database_url:
        msg = "DATABASE_URL is not configured."
        raise DatabaseConnectionError(msg)

    try:
        engine = engine_factory(settings.database_url)
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except SQLAlchemyError as exc:
        msg = f"Database connection failed: {exc}"
        raise DatabaseConnectionError(msg) from exc
