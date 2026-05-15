from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(title="government-cabinet-bid-agent-api")

    @app.get("/health")
    def health() -> dict[str, str]:
        return {
            "status": "ok",
            "service": "government-cabinet-bid-agent-api",
        }

    return app


app = create_app()

