from fastapi import APIRouter, Depends
from controllers.album_controller import create, get_all, get_by_id, delete_by_id
from config.database import get_db
from sqlalchemy.orm import Session
from schemas.album_schema import Album

albums_router = APIRouter(
    prefix="/albums",
    tags=["Albums"],
)

@albums_router.get("/", tags=["Albums"], response_model=list[Album])
def get_all_albums(db: Session = Depends(get_db)):
    return get_all(db)

@albums_router.post("/createalbums", tags=["Albums"], response_model=list[Album])
def create_albums(albums: list[Album], db: Session = Depends(get_db)):
    for album in albums:
        create(db, album)
    return albums

@albums_router.post("/create", tags=["Albums"], response_model=Album)
def create_album(album: Album, db: Session = Depends(get_db)):
    return create(db, album)

@albums_router.get("/{album_id}",tags=['Albums'], response_model=Album)
def get_user_by_id(album_id: str, db: Session = Depends(get_db)):
    return get_by_id(db, album_id) 

@albums_router.delete("/{album_id}", tags=['Albums'])
def delete_user_by_id(album_id: str, db: Session = Depends(get_db)):
    return delete_by_id(db, album_id)



