from sqlalchemy.orm import Session
from models.track_model import Track
from schemas.track_schema import Track as TrackSchema

def create(db: Session, track: TrackSchema):
    db_track = Track(
        id=track.id,
        uri = track.uri,
        name=track.name,
        duration=track.duration,
        explicit=track.explicit,
        cover=track.cover,
        album_id=track.album_id
    )
    db.add(db_track)
    db.commit()
    db.refresh(db_track)
    return db_track

def get_all(db: Session):
    return db.query(Track).all()

def get_by_id(db: Session, track_id: str):
    return db.query(Track).filter(Track.id == track_id).first()

def delete_by_id(db: Session, track_id: str):
    db.query(Track).filter(Track.id == track_id).delete()
    db.commit()
    return {"message": f"Track with id {track_id} deleted successfully"}