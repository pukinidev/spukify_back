from fastapi import APIRouter, Depends
from config.database import get_db
from sqlalchemy.orm import Session
from controllers.user_controller import create, delete_by_id, get_all, get_by_id
from schemas.user_schema import User

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

@router.post("/create", tags=["Users"], response_model=User)
def create_user(user: User, db: Session = Depends(get_db)):
    return create(db, user)

@router.get("/{user_id}", tags=["Users"], response_model=User)
def get_user_by_id(user_id: str, db: Session = Depends(get_db)):
    return get_by_id(db, user_id) 

@router.get("/", tags=["Users"], response_model=list[User])
def get_all_users(db: Session = Depends(get_db)):
    return get_all(db)

@router.delete("/{user_id}", tags=["Users"])
def delete_user_by_id(user_id: str, db: Session = Depends(get_db)):
    return delete_by_id(db, user_id)


