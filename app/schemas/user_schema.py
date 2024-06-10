from pydantic import BaseModel

class User(BaseModel):
    id: str
    email: str
    username: str
    image: str

    class Config:
        from_attributes = True
