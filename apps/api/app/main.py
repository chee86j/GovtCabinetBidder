from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.db.session import DatabaseConnectionError, check_database_connection


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name)
    cors_origins = settings.cors_origin_list()

    if cors_origins:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=cors_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    @app.get("/health")
    def health() -> dict[str, str]:
        return {
            "status": "ok",
            "service": settings.app_name,
        }

    @app.get("/health/db")
    def health_db() -> JSONResponse:
        try:
            check_database_connection(settings)
        except DatabaseConnectionError as exc:
            return JSONResponse(
                status_code=503,
                content={
                    "status": "error",
                    "database": "disconnected",
                    "detail": str(exc),
                },
            )

        return JSONResponse(
            status_code=200,
            content={
                "status": "ok",
                "database": "connected",
            },
        )

    return app


app = create_app()
