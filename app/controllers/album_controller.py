from sqlalchemy.orm import Session
from models.album_model import Album
from schemas.album_schema import Album as AlbumSchema

def create(db: Session, album: AlbumSchema):
    db_album = Album(
        id=album.id,
        uri = album.uri,
        name=album.name,
        cover=album.cover,
        album_type=album.album_type
    )
    db.add(db_album)
    db.commit()
    db.refresh(db_album)
    return db_album

def get_all(db: Session):
    return db.query(Album).all()

