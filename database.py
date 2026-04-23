


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# DBとの接続を作る
engine = create_engine("postgresql://postgres:hal192@localhost:5432/postgres")



# リクエストの度にsessionを作り、DBに命令する
# そのSessionを作る工場がSessionLocal
# sessionmakerで「こういう設定」のSessionLocalを作る
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine)
# テーブルの設計図の親クラス
# これを継承し、子クラスでテーブルをつくることで初めてテーブルになる
Base = declarative_base()



