from typing import List

from sqlalchemy import (
    Column,
    Integer,
    String,
    BOOLEAN
)
from sqlalchemy.ext.declarative import declarative_base

from pydantic import BaseModel

from database.database_adapter import engine

Base = declarative_base()


class DataUser(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)

    role = Column(String)
    public_key = Column(String)
    private_key = Column(String)


class DataMarketplaceItem(Base):
    __tablename__ = 'Market'

    id = Column(Integer, primary_key=True)

    type = Column(String)
    title = Column(String)
    description = Column(String)
    date = Column(String)
    cost = Column(Integer)
    photo = Column(String)

Base.metadata.create_all(engine)


# _________________________________ TODO здесь мы дублируем модели, как иначе сделать хз, мб лучше можно

class BaseUser(BaseModel):
    role: str
    public_key: str
    private_key: str

    class Config:
        orm_mode = True


class UserSeries(BaseModel):
    number_of_users: int = 0
    series: List[BaseUser] = []


class BaseMarketplaceItem(BaseModel):
    type: str
    title: str
    description: str
    date: str
    cost: int
    photo: str

    class Config:
        orm_mode = True