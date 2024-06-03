from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import relationship
from config.database import Base

artist_albums = Table('artists_albums', Base.metadata, 
    Column('artist_id', String, ForeignKey('artists.id')),
    Column('album_id', String, ForeignKey('albums.id'))
)

class Artist(Base):
    __tablename__ = "artists"
    id = Column(String, primary_key=True)
    uri = Column(String, unique=True)
    name = Column(String)
    artist_image = Column(String)
    tracks = relationship("Track", secondary="artists_tracks", back_populates="artists")
    albums = relationship("Album", secondary="artists_albums", back_populates="artists")