from fastapi import APIRouter

health_route = APIRouter(tags=["health"])


@health_route.get("/health")
def health():
    return {"status": "ok"}
