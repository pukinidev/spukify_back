from pydantic import BaseModel

class Artist(BaseModel):
    id: str
    name: str

    class Config:
        from_attributes = True