from fastapi import APIRouter

router = APIRouter(
    prefix="/albums",
    tags=["Albums"],
    responses={404: {"description": "Not found"}},
)