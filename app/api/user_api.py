from fastapi import FastAPI, Depends
from config.database import get_db
from sqlalchemy.orm import Session
from controllers.user_controller import create, delete_by_id, get_all, get_by_id
from schemas.user_schema import User
from models import user_model
from config.database import engine

usersapi = FastAPI()

# Create User Table
user_model.Base.metadata.create_all(bind=engine)

@usersapi.post("/create", response_model=User)
def create_user(user: User, db: Session = Depends(get_db)):
    return create(db, user)

@usersapi.get("/{user_id}", response_model=User)
def get_user_by_id(user_id: str, db: Session = Depends(get_db)):
    return get_by_id(db, user_id) 

@usersapi.get("/", response_model=list[User])
def get_all_users(db: Session = Depends(get_db)):
    return get_all(db)

@usersapi.delete("/{user_id}")
def delete_user_by_id(user_id: str, db: Session = Depends(get_db)):
    return delete_by_id(db, user_id)
