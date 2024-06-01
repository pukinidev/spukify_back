from fastapi import APIRouter, Depends
from controllers.artist_controller import create, delete_by_id, get_all, get_by_id
from config.database import get_db
from sqlalchemy.orm import Session
from schemas.artist_schema import Artist

artists_router = APIRouter(
    prefix="/artists",
    tags=['Artists'],
)

@artists_router.post("/create", tags=['Artists'], response_model=Artist)
def create_artist(artist: Artist, db: Session = Depends(get_db)):
    return create(db, artist)

@artists_router.get("/", tags=['Artists'], response_model=list[Artist])
def get_all_artists(db: Session = Depends(get_db)):
    return get_all(db)

@artists_router.get("/{artist_id}", tags=['Artists'], response_model=Artist)
def get_artist_by_id(artist_id: int, db: Session = Depends(get_db)):
    return get_by_id(db, artist_id)

@artists_router.delete("/{artist_id}", tags=['Artists'])
def delete_artist_by_id(artist_id: int, db: Session = Depends(get_db)):
    return delete_by_id(db, artist_id)
