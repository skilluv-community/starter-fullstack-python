# Architecture — starter-fullstack-python

## Choix opinionated

### 1. FastAPI + Pydantic v2

- ASGI natif, async-first.
- OpenAPI auto sur `/docs` et `/redoc`.
- Pydantic v2 rapide, `model_config` clean, intégration `pydantic-settings`.

### 2. SQLAlchemy 2 avec `DeclarativeBase` typé

- API `Mapped[T]` / `mapped_column` moderne.
- Pas de relations lazy inattendues à la requête.

### 3. Alembic pour les migrations

- Autogenerate depuis les modèles.
- Lancé au démarrage du conteneur (`alembic upgrade head`).

### 4. `psycopg` v3

- Driver Postgres current-gen, remplace `psycopg2`.
- Support async natif quand nécessaire.

### 5. `uv` comme package manager unique

- Rapide, lockfile, remplace pip + venv + pip-tools.
- `uv sync --frozen` en CI.

### 6. Ruff + mypy strict

- Ruff = lint + format rapide (remplace black + isort + flake8).
- Mypy strict pour la sûreté de type réelle.

## Hors scope

- Auth (`fastapi-users` ou IdP externe).
- Jobs asynchrones (Celery, RQ, Dramatiq).
- Endpoints async — la démo utilise SQLAlchemy sync pour la simplicité. Passer à `AsyncSession` pour la concurrence.
