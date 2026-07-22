# Démarrage — starter-fullstack-python

## Prérequis

- Docker + Docker Compose 2.24+
- (Optionnel, dev local) Python 3.12+, [uv](https://docs.astral.sh/uv/), Node 22/24 LTS, PostgreSQL 18

## Premier lancement

```bash
git clone git@github.com:skilluv-community/starter-fullstack-python.git
cd starter-fullstack-python
cp .env.example .env
docker compose up --build
```

Alembic exécute `alembic upgrade head` au boot du conteneur, le schéma est appliqué auto.

- Frontend : <http://localhost:5173>
- Health backend : <http://localhost:3001/health>
- Docs OpenAPI : <http://localhost:3001/docs>

## Modifier le code

- **Backend** (`backend/`) : éditer `backend/app/`. Le hot-reload n'est pas actif dans le conteneur ; pour ça, lancer `uv run uvicorn app.main:app --reload` localement.
- **Frontend** (`frontend/`) : HMR Vite auto.
- **Schéma DB** : éditer les modèles puis générer une migration :

```bash
cd backend
uv run alembic revision --autogenerate -m "changement"
```

Puis commit le fichier sous `backend/alembic/versions/`.

## Tests

```bash
make test
```

Les tests backend utilisent `TestClient` de FastAPI — pas besoin de DB live.

## Déploiement

Coolify sur le repo. En prod :

- Pas de `--reload`
- Vrai `POSTGRES_PASSWORD`
- Restreindre `CORS_ORIGIN`
