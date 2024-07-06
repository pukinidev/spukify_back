from sqlalchemy.orm import Session
from models.user_model import User
from schemas.user_schema import User as UserSchema

def create(db: Session, user: UserSchema):
    db_user = User(
        id=user.id,
        email=user.email,
        username=user.username,
        image=user.image
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all(db: Session):
    return db.query(User).all()

def get_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()

def delete_by_id(db: Session, user_id: str):
    db.query(User).filter(User.id == user_id).delete()
    db.commit()
    return {"message": f"User with id {user_id} deleted successfully"}