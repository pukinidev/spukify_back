from fastapi import FastAPI
from fastapi import FastAPI, Depends
from controllers.artist_controller import create, delete_by_id, get_all, get_by_id
from config.database import get_db
from sqlalchemy.orm import Session
from schemas.artist_schema import Artist
from config.database import engine

artistsapi = FastAPI()

@artistsapi.post("/create", response_model=Artist)
def create_artist(artist: Artist, db: Session = Depends(get_db)):
    return create(db, artist)

@artistsapi.get("/")
def get_all_artists(db: Session = Depends(get_db)):
    return get_all(db)

@artistsapi.get("/{artist_id}", response_model=Artist)
def get_artist_by_id(artist_id: int, db: Session = Depends(get_db)):
    return get_by_id(db, artist_id)

@artistsapi.delete("/{artist_id}")
def delete_artist_by_id(artist_id: int, db: Session = Depends(get_db)):
    return delete_by_id(db, artist_id)




