from pydantic import BaseModel

class Artist(BaseModel):
    id: str
    uri: str
    name: str
    image: str

    class Config:
        from_attributes = True