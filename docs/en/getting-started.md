# Getting started — starter-fullstack-python

## Prerequisites

- Docker + Docker Compose 2.24+
- (Optional, local dev) Python 3.12+, [uv](https://docs.astral.sh/uv/), Node 22/24 LTS, PostgreSQL 18

## First run

```bash
git clone git@github.com:skilluv-community/starter-fullstack-python.git
cd starter-fullstack-python
cp .env.example .env
docker compose up --build
```

Alembic runs `alembic upgrade head` at startup, so the DB schema is applied automatically.

- Frontend at <http://localhost:5173>
- Backend health at <http://localhost:3001/health>
- OpenAPI docs at <http://localhost:3001/docs>

## Making changes

- **Backend** (`backend/`): edit code under `backend/app/`. uvicorn `--reload` isn't the default in the container — for hot-reload, run `uv run uvicorn app.main:app --reload` locally instead.
- **Frontend** (`frontend/`): Vite HMR reloads automatically.
- **DB schema**: edit models under `backend/app/models/` then generate a new migration:

```bash
cd backend
uv run alembic revision --autogenerate -m "your change"
```

Then commit the file under `backend/alembic/versions/`.

## Running tests

```bash
make test
```

Backend tests use FastAPI's TestClient — no live DB required by default.

## Deploying

Point Coolify at the repo. In production:

- Turn off `uvicorn --reload` (already off)
- Set a strong `POSTGRES_PASSWORD`
- Restrict `CORS_ORIGIN` to your frontend URL
