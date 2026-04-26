
from sqlalchemy import Column,Integer,String
from database import Base


# DBで作ったBaseを継承し、子クラスでテーブルを作る
class User(Base):
    __tablename__ = 'users'
    id = Column('id',Integer,primary_key = True)
    name = Column('name',String(50))
    email = Column('email',String(100))
    password = Column('password',String(255))





