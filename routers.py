

from fastapi import APIRouter
from crud import create_user
from database import SessionLocal
from fastapi import Depends
from schemas import UserCreate
from database import SessionLocal
from sqlalchemy.orm import Session
from crud import create_user, get_users,update_user,delete_user

router = APIRouter()


# エンドポイントは「このURLでこの処理をする」という窓口
#　ユーザーがUIで操作した内容を定義する

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.login("/users/login")
async def login_user_endpoint(user:UserCreate):
    return 


@router.post("/users")
async def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db,user)


@router.get("/users")
async def get_users_endpoint(db: Session = Depends(get_db)):
    return get_users(db)


@router.put("/users/{user_id}")
async def update_user_endpoint(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return update_user(db,user_id,user)

@router.delete("/users/{user_id}")
async def delete_user_endpoint(user_id: int,db: Session = Depends(get_db)):
    return delete_user(db,user_id)
