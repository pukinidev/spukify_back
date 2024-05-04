from fastapi import APIRouter

router = APIRouter(
    prefix="/tracks",
    tags=["Tracks"],
    responses={404: {"description": "Not found"}},
)