from pydantic import BaseModel

class Track(BaseModel):
    id: str
    uri: str
    name: str
    duration: int
    explicit: bool
    cover: str
    album_id: str
    
    class Config:
        from_attributes = True