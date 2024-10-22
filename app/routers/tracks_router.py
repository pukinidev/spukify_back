from fastapi import  Depends, APIRouter
from config.database import get_db
from sqlalchemy.orm import Session
from controllers.tracker_controller import create, get_all, get_by_id, delete_by_id
from schemas.track_schema import Track

tracks_router = APIRouter(
    prefix="/tracks",
    tags=["Tracks"],
)

@tracks_router.get("/",tags=['Tracks'], response_model=list[Track])
def get_all_tracks(db: Session = Depends(get_db)):
    return get_all(db)

@tracks_router.post("/create", tags=["Tracks"], response_model=Track)
def create_track(track: Track, db: Session = Depends(get_db)):
    return create(db, track)

@tracks_router.post("/createtracks", tags=["Tracks"], response_model=list[Track])
def create_tracks(tracks: list[Track], db: Session = Depends(get_db)):
    for track in tracks:
        create(db, track)
    return tracks

@tracks_router.get("/{track_id}",tags=['Tracks'], response_model=Track)
def get_user_by_id(track_id: str, db: Session = Depends(get_db)):
    return get_by_id(db, track_id) 

@tracks_router.delete("/{track_id}", tags=['Tracks'])
def delete_user_by_id(track_id: str, db: Session = Depends(get_db)):
    return delete_by_id(db, track_id)