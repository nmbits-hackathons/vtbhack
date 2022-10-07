from typing import Optional, Union

from database.models import BaseUser, UserSeries, DataUser, ResponseUser
from database.database_adapter import create_session

from sqlalchemy import or_
from sqlalchemy import and_


class UserDatabaseAdapter:
    @staticmethod
    def create_user(user_model: BaseUser) -> int:
        print('call create_user fun\n', user_model)
        with create_session() as session:
            user = DataUser(**user_model.dict())
            session.add(user)
            session.flush()
            user_id = user.id
        return user_id

    @staticmethod
    def delete_user(user_id: int) -> None:
        with create_session() as session:
            user = session.query(DataUser).filter(DataUser.id == user_id).delete()

    @staticmethod
    def update_user(user_id: int) -> None:
        pass

    @staticmethod
    def get_user_by_id(post_id: int) -> Union[BaseUser, None]:
        with create_session() as session:
            user_model = session.query(DataUser).get(post_id)
            if user_model is None:
                post = None
            else:
                post = BaseUser.from_orm(user_model)
        return post

    @staticmethod
    def get_users_list(left: int, right: int) -> Union[ResponseUser, None]:
        with create_session() as session:
            data_list = session.query(DataUser)[left:right]
            user_series = UserSeries()
            for data_user in data_list:
                user_series.series.append(ResponseUser.from_orm(data_user))
                user_series.number_of_users += 1

        return user_series
