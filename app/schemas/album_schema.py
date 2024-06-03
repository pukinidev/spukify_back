from pydantic import BaseModel
import enum

class AlbumType(str, enum.Enum):
    album = "album"
    single = "single"
    compilation = "compilation"

class Album(BaseModel):
    id: str
    uri: str
    name: str
    cover: str
    album_type: AlbumType 
    
    class Config:
        from_attributes = True