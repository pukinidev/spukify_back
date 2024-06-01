from fastapi import APIRouter, Depends
from config.database import get_db
from sqlalchemy.orm import Session
from controllers.user_controller import create
from schemas.user_schema import User

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

@router.post("/createuser", tags=["Users"], response_model=User)
def create_user(user: User, db: Session = Depends(get_db)):
    return create(db, user)
