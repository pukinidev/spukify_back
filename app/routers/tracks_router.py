from fastapi import APIRouter

tracks_router = APIRouter(
    prefix="/tracks",
    tags=["tracks"],
)
