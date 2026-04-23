


from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate,UserLogin
from auth import hash_password

# CRUDはDBへの操作のこと
#routersではエンドポイントへのリクエストを元にcrudの操作をする

#　新しいユーザーデータを作る

# schemasからUserCreateを呼んでるため
def create_user(db: Session,user:UserCreate):
    db_user = User(name=user.name,email=user.email,password=hash_password(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# ユーザー情報を取得する
def get_users(db: Session):
    users = db.query(User).all()
    return users

# ユーザー情報を更新する
def update_user(db: Session,user_id: int, user:UserCreate):
    db_user = db.query(User).filter(User.id == user_id).first()
    db_user.name = user.name
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return {"message":"deleted"}


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

    

