from sqlalchemy.orm import Session
from models.user_model import User
from schemas.user_schema import User as UserSchema

def create(db: Session, user: UserSchema):
    db_user = User(
        id=user.id,
        email=user.email,
        user_name=user.user_name,
        profile_picture=user.profile_picture
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user