from fastapi import APIRouter, Depends
from controllers.album_controller import create, get_all
from config.database import get_db
from sqlalchemy.orm import Session
from schemas.album_schema import Album

albums_router = APIRouter(
    prefix="/albums",
    tags=["Albums"],
)

@albums_router.post("/create", tags=["albums"], response_model=Album)
def create_album(album: Album, db: Session = Depends(get_db)):
    return create(db, album)

@albums_router.get("/", tags=["albums"], response_model=list[Album])
def get_all_albums(db: Session = Depends(get_db)):
    return get_all(db)


