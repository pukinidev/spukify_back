from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from config.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    email = Column(String, unique=True, index=True)
    user_name = Column(String, unique=True, index=True)
    profile_picture = Column(String)
    