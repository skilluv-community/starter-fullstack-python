# Architecture — starter-fullstack-python

## Opinionated choices

### 1. FastAPI + Pydantic v2

- ASGI-native, async-first.
- Automatic OpenAPI at `/docs` and `/redoc`.
- Pydantic v2 gives fast validation, `model_config` for behavior, and integrates cleanly with `pydantic-settings`.

### 2. SQLAlchemy 2 with the typed `DeclarativeBase`

- Modern `Mapped[T]` / `mapped_column` API.
- No lazy relationships surprising you at request time.

### 3. Alembic for migrations

- Autogenerate from model changes.
- Runs at container startup (`alembic upgrade head`).

### 4. `psycopg` v3

- The current-generation Postgres driver, replaces `psycopg2`.
- Supports async natively when you need it.

### 5. `uv` as the sole package manager

- Fast, lockfile-based, replaces pip + venv + pip-tools.
- `uv sync --frozen` in CI.

### 6. Ruff + mypy strict

- Ruff = fast lint + format (replaces black + isort + flake8).
- Mypy strict for real type safety.

## What's out of scope

- Auth (add `fastapi-users` or an external IdP).
- Background jobs (Celery, RQ, or Dramatiq if needed).
- Async endpoints for now — the sample uses sync SQLAlchemy for simplicity. Switch to `AsyncSession` when you need concurrency.
