from database import Base
from database import engine
from fastapi import FastAPI

from routers import router

Base.metadata.create_all(bind=engine)



app = FastAPI()
app.include_router(router)
# /にGETリクエストが来たら、下の関数を実行する


# async で非同期にする　非同期とはWebサーバーが
# 他のリクエストを受け付けるという意味
# 同期は処理中受け付けない



