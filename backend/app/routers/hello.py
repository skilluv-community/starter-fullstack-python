from datetime import UTC, datetime

from fastapi import APIRouter

router = APIRouter(prefix="/api")


@router.get("/hello")
def hello(name: str | None = None) -> dict[str, str]:
    who = (name or "").strip() or "Skilluv"
    return {
        "message": f"Hello {who}!",
        "server_time": datetime.now(UTC).isoformat(),
    }
