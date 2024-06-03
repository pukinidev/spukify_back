from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from config.database import Base

track_artists = Table('artists_tracks', Base.metadata, 
    Column('track_id', String, ForeignKey('tracks.id')),
    Column('artist_id', String, ForeignKey('artists.id'))
)


class Track(Base):
    __tablename__ = "tracks"
    id = Column(String, primary_key=True)
    uri = Column(String, unique=True)
    name = Column(String)
    duration = Column(Integer)
    explicit = Column(Boolean)
    cover = Column(String)
    album_id = Column(String, ForeignKey("albums.id"))
    album = relationship("Album", back_populates="tracks")
    artists = relationship("Artist", secondary="artists_tracks", back_populates="tracks")
