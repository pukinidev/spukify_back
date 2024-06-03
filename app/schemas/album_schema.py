from pydantic import BaseModel

class Album(BaseModel):
    id: str
    uri: str
    name: str
    cover: str
    album_type: str
    
    class Config:
        from_attributes = True