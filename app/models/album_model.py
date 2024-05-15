from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base
import enum

class Album(Base):
    __tablename__ = "albums"
    id = Column(String, primary_key=True)
    name = Column(String)
    cover = Column(String)
    artists = relationship("Artist", secondary="artist_albums", back_populates="albums")
  