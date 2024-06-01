from pydantic import BaseModel

class User(BaseModel):
    id: str
    email: str
    user_name: str
    profile_picture: str

    class Config:
        from_attributes = True
