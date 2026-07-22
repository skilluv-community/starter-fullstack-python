.PHONY: dev test lint build fmt clean help

help:
	@echo "Targets:"
	@echo "  dev    — docker compose up"
	@echo "  test   — pytest + vitest"
	@echo "  lint   — ruff + mypy + eslint + svelte-check"
	@echo "  build  — production build for frontend"
	@echo "  fmt    — auto-format"
	@echo "  clean  — remove build artifacts"

dev:
	docker compose up --build

test:
	cd backend && uv run pytest -q
	cd frontend && npm run test:unit -- --run

lint:
	cd backend && uv run ruff check . && uv run mypy app
	cd frontend && npm run lint && npm run check

build:
	cd frontend && npm run build

fmt:
	cd backend && uv run ruff format .
	cd frontend && npm run format

clean:
	rm -rf backend/.venv backend/.pytest_cache backend/.ruff_cache backend/.mypy_cache
	rm -rf frontend/node_modules frontend/build frontend/.svelte-kit
