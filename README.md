# starter-fullstack-python

> A Skilluv starter — FastAPI + SQLAlchemy 2 + Alembic + PostgreSQL 18, SvelteKit 5 frontend.

[![CI](https://github.com/skilluv-community/starter-fullstack-python/actions/workflows/ci.yml/badge.svg)](https://github.com/skilluv-community/starter-fullstack-python/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![Skilluv](https://img.shields.io/badge/skilluv-community-emerald)](https://skilluv.io)

## English

### What this is

- **Backend**: Python 3.12 + FastAPI + SQLAlchemy 2 + Alembic + `psycopg` v3 + Pydantic v2, managed with **uv**
- **Frontend**: SvelteKit 5 (runes) + Tailwind v4
- **Orchestration**: Docker Compose (postgres + backend + frontend)
- **Tests**: pytest + ruff + mypy strict + Vitest + Playwright

### Quickstart

```bash
git clone git@github.com:skilluv-community/starter-fullstack-python.git
cd starter-fullstack-python
cp .env.example .env
docker compose up --build
```

- Frontend: <http://localhost:5173>
- Backend: <http://localhost:3001/health>
- Interactive docs: <http://localhost:3001/docs>

### Structure

```
backend/     FastAPI app + SQLAlchemy models + Alembic migrations
frontend/    SvelteKit app (Svelte 5 runes, Tailwind v4)
docs/        Bilingual docs (fr, en)
.github/     CI + dependabot + PR template
```

### What's inside

- `GET /health` — liveness probe
- `GET /api/hello?name=Ada` — greeting endpoint
- `GET/POST/DELETE /api/notes` — CRUD demo (SQLAlchemy + PostgreSQL)
- SvelteKit pages `/` and `/notes`

### Docs

- [`docs/en/getting-started.md`](./docs/en/getting-started.md)
- [`docs/en/architecture.md`](./docs/en/architecture.md)

---

## Français

Starter fullstack Python (FastAPI) + SvelteKit prêt-à-l'emploi. Voir [`docs/fr/getting-started.md`](./docs/fr/getting-started.md) et [`docs/fr/architecture.md`](./docs/fr/architecture.md).

```bash
git clone git@github.com:skilluv-community/starter-fullstack-python.git
cd starter-fullstack-python
cp .env.example .env
docker compose up --build
```

---

## License

MIT — see [LICENSE](./LICENSE).

## Related

- [Skilluv](https://skilluv.io)
- [Skilluv Community Charter](https://github.com/skilluv-community/community-charter)
- [Other starters](https://github.com/orgs/skilluv-community/repositories?q=starter)
