from fastapi import  Depends
from config.database import get_db
from sqlalchemy.orm import Session
from controllers.user_controller import create, delete_by_id, get_all, get_by_id
from schemas.user_schema import User
from fastapi import APIRouter

users_router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@users_router.get("/",tags=['Users'], response_model=list[User])
def get_all_users(db: Session = Depends(get_db)):
    return get_all(db)

@users_router.post("/createusers", tags=['Users'], response_model=list[User])
def create_users(users: list[User], db: Session = Depends(get_db)):
    for user in users:
        create(db, user)
    return users

@users_router.post("/create", tags=['Users'] ,response_model=User)
def create_user(user: User, db: Session = Depends(get_db)):
    return create(db, user)



@users_router.get("/{user_id}",tags=['Users'], response_model=User)
def get_user_by_id(user_id: str, db: Session = Depends(get_db)):
    return get_by_id(db, user_id) 

@users_router.delete("/{user_id}", tags=['Users'])
def delete_user_by_id(user_id: str, db: Session = Depends(get_db)):
    return delete_by_id(db, user_id)
