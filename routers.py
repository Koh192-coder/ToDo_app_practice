


from database import SessionLocal
from fastapi import HTTPException,APIRouter,Depends
from schemas import UserCreate,UserLogin
from database import SessionLocal
from sqlalchemy.orm import Session
import crud
import auth
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

# エンドポイントは「このURLでこの処理をする」という窓口
#　ユーザーがUIで操作した内容を定義する

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Depends()で引数の関数の結果が渡される Dependはリクエストの度にSessionが生成され、破棄する
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    email = auth.verify_token(token)
    user = crud.get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=401, detail="ユーザーが見つかりません")
    return user

@router.post("/users/login")
async def login_user_endpoint(user: UserLogin, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if not db_user:
        raise HTTPException(status_code=401, detail="メールアドレスが違います")
    if not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="パスワードが違います")
    token = auth.create_access_token({"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/users")
async def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.get("/users")
async def get_users_endpoint(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return crud.get_users(db)

@router.put("/users/{user_id}")
async def update_user_endpoint(user_id: int, user: UserCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return crud.update_user(db, user_id, user)

@router.delete("/users/{user_id}")
async def delete_user_endpoint(user_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return crud.delete_user(db, user_id)





    