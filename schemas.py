



# ユーザーが入力する際の入力ルールを定義する
from pydantic import BaseModel

# pydanticのBaseModelは入力データの型をチェックしてくれる
# 変なリクエストが来たときは自動ではじく

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

# ログインのスキーマ nameは必要ないため省く
class UserLogin(BaseModel):
    email: str
    password: str