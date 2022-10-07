from typing import Any, Optional, Union

from database.models import DataMarketplaceItem, BaseMarketplaceItem
from database.database_adapter import create_session

# from sqlalchemy import or_
# from sqlalchemy import and_


class MarketDatabaseAdapter:
    @staticmethod
    def create_item(item_model: BaseMarketplaceItem) -> int:
        print('call create_market_item fun\n', item_model)
        with create_session() as session:
            item = DataMarketplaceItem(**item_model.dict())
            session.add(item)
            session.flush()
            item_id = item.id
        return item_id

    @staticmethod
    def get_item_by_id(post_id: int) -> Union[BaseMarketplaceItem, None]:
        with create_session() as session:
            item_model = session.query(DataMarketplaceItem).get(post_id)
            if item_model is None:
                post = None
            else:
                post = BaseMarketplaceItem.from_orm(item_model)
        return post

    @staticmethod
    def get_items() -> Any:
        with create_session() as session:
            item_models = session.query(DataMarketplaceItem).all()
            if item_models is None:
                posts = None
            else:
                posts = [BaseMarketplaceItem.from_orm(item_model) for item_model in item_models]
        return posts

    @staticmethod
    def delete_item(item_id: int) -> None:
        with create_session() as session:
            item = session.query(DataMarketplaceItem).filter(DataMarketplaceItem.id == item_id).delete()




    # @staticmethod
    # def update_user(user_id: int) -> None:
    #     pass


    # @staticmethod
    # def get_users_list(left:int,right:int) -> Union[BaseUser, None]:
    #     with create_session() as session:
    #         data_list = session.query(DataUser)[left:right]
    #         user_series = UserSeries()
    #         for data_user in data_list:
    #             user_series.series.append(BaseUser.from_orm(data_user))

    #     return user_series
