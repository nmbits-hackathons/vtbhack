import datetime
from typing import List, Optional

from sqlalchemy import (
    Column,
    Integer,
    String,
    BOOLEAN,
    DATETIME
)
from sqlalchemy.ext.declarative import declarative_base

from pydantic import BaseModel

from database.database_adapter import engine

Base = declarative_base()


class DataUser(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)

    admin_role = Column(BOOLEAN)
    permission_nft_release = Column(BOOLEAN)
    permission_transfer_treasury = Column(BOOLEAN)  # from treasury to people
    permission_moderate_marketplace = Column(BOOLEAN)
    permission_events = Column(BOOLEAN)

    public_key = Column(String)
    private_key = Column(String)

    name = Column(String)
    email = Column(String)  # unique=True)


class DataEvent(Base):
    __tablename__ = 'Post'

    id = Column(Integer, primary_key=True)

    title = Column(String)
    description = Column(String)
    date_publication = Column(DATETIME)
    date_event = Column(DATETIME)
    creator = Column(Integer)  # id of creator user
    type = Column(String)
    reward = Column(Integer)


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
    admin_role: bool
    permission_nft_release: bool
    permission_transfer_treasury: bool  # from treasury to people
    permission_moderate_marketplace: bool
    permission_events: bool

    public_key: str
    private_key: str

    name: str
    email: str

    class Config:
        orm_mode = True


class ResponseUser(BaseUser):
    id: int

    class Config:
        orm_mode = True


class UserSeries(BaseModel):
    number_of_users: int = 0
    series: List[ResponseUser] = []


class BaseEvent(BaseModel):
    title: str
    description: Optional[str]
    date_publication: Optional[datetime.datetime]
    date_event: Optional[datetime.datetime]
    creator: Optional[int]  # id of creator user
    type: Optional[str]
    reward: Optional[int]

    class Config:
        orm_mode = True


class ResponseEvent(BaseEvent):
    id: int

    class Config:
        orm_mode = True


class EventSeries(BaseModel):
    number_of_events: int = 0
    series: List[ResponseEvent] = []


class BaseMarketplaceItem(BaseModel):
    type: str
    title: str
    description: str
    date: str
    cost: int
    photo: str

    class Config:
        orm_mode = True
        orm_mode = True
