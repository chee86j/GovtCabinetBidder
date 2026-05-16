# government-cabinet-bid-agent

This MVP is a government bid intelligence and partner-matching dashboard for companies that work on cabinet, countertop, casework, vanity, public housing rehab, and unit-turnover bids.

The project will help users find relevant public-sector opportunities, understand bid requirements, and identify potential partners for pursuing the work.

## Structure

```text
apps/
  api/
  web/
docs/
scripts/
```

The repository is intentionally minimal for now. Tooling, frameworks, and dependencies should be added only when the MVP needs them.

## Backend

Create the virtual environment and install the API dependencies:

```bash
cd apps/api
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

Run the backend locally:

```bash
cd apps/api
source .venv/bin/activate
uvicorn app.main:app --reload
```

Run the backend tests:

```bash
cd apps/api
source .venv/bin/activate
pytest
```

The health check is available at `http://localhost:8000/health`.

## Frontend

Install the frontend dependencies:

```bash
cd apps/web
npm install
```

Run the frontend locally:

```bash
cd apps/web
npm run dev
```

Build the frontend:

```bash
cd apps/web
npm run build
```

Lint the frontend:

```bash
cd apps/web
npm run lint
```
