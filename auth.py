

from passlib.context import CryptContext
from jose import jwt,JWTError
from datetime import datetime, timedelta,timezone
from fastapi import HTTPException
from dotenv import load_dotenv
import os

load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# SECRET_KEY は鍵、ALGORITHM は鍵の使い方

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"


# jwd.encode でトークン生成する
# 期限の設定、現在時刻 + 30分し、期限をto_encodeに追加

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# .encode はヘッダー・ペイロード・署名 の3のパーツを作り、それぞれをBase64でエンコード
# .でつなげて１つの文字列にして返す


def verify_token(token:str):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="無効なトークンです")

        return email
    except JWTError:
        raise HTTPException(status_code=401, detail="トークンが不正です")
    
