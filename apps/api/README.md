# government-cabinet-bid-agent-api

Minimal FastAPI backend for the government cabinet bid agent MVP.

## Available route

- `GET /health` returns service health for local checks and tests.

## Database migrations

Run Alembic migrations from `apps/api`:

```bash
alembic revision -m "your_migration_name"
alembic upgrade head
```
