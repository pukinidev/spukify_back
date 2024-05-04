from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from config.database import Base

artist_albums = Table('artist_albums', Base.metadata, 
    Column('artist_id', String, ForeignKey('artists.id')),
    Column('album_id', String, ForeignKey('albums.id'))
)

class Artist(Base):
    __tablename__ = "artists"
    id = Column(String, primary_key=True)
    name = Column(String)
    tracks = relationship("Track", secondary="track_artists", back_populates="artists")
    albums = relationship("Album", secondary="artist_albums", back_populates="artists")