from fastapi import APIRouter

router = APIRouter(
    prefix="/artists",
    tags=["Artists"],
    responses={404: {"description": "Not found"}},
)