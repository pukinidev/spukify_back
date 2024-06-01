from sqlalchemy.orm import Session
from models.artist_model import Artist
from schemas.artist_schema import Artist as ArtistSchema

def create(db: Session, artist: ArtistSchema):
    db_artist = Artist(
        id=artist.id,
        uri = artist.uri,
        name=artist.name,
        artist_image=artist.artist_image
    )
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist

def get_all(db: Session):
    return db.query(Artist).all()

def get_by_id(db: Session, artist_id: str):
    return db.query(Artist).filter(Artist.id == artist_id).first()

def delete_by_id(db: Session, artist_id: str):
    db.query(Artist).filter(Artist.id == artist_id).delete()
    db.commit()
    return {"message": "Artist deleted successfully"}