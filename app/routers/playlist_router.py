from fastapi import APIRouter

router = APIRouter(
    prefix="/playlists",
    tags=["Playlists"],
    responses={404: {"description": "Not found"}},
)