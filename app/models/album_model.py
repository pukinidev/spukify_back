from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
from config.database import Base
import enum 

class AlbumType(enum.Enum):
    single = "single"
    album = "album"
    compilation = "compilation"

class Album(Base):
    __tablename__ = "albums"
    id = Column(String, unique=True,primary_key=True)
    uri = Column(String, unique=True)
    name = Column(String)
    cover = Column(String)
    album_type = Column(Enum(AlbumType))
    artists = relationship("Artist", secondary="artist_albums", back_populates="albums")
    tracks = relationship("Track", back_populates="album")
  