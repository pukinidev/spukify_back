from fastapi import FastAPI
from fastapi import FastAPI, Depends
from controllers.artist_controller import create
from config.database import get_db
from sqlalchemy.orm import Session
from schemas.artist_schema import Artist
from config.database import engine


artistsapi = FastAPI()

@artistsapi.post("/create", response_model=Artist)
def create_artist(artist: Artist, db: Session = Depends(get_db)):
    return create(db, artist)



