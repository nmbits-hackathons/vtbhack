from fastapi import (
    APIRouter,
    Depends,
    status,
    Request,
    HTTPException
)

from database.models import BaseUser
from database.models import BaseMarketplaceItem
from marketplace.market_base_adapter import MarketDatabaseAdapter


router = APIRouter(
    prefix='/marketplace',
    tags=['marketplace'],
)


@router.get('/get_items/')
def get_items():
    items = MarketDatabaseAdapter.get_items()
    if items is None:
        raise HTTPException(status_code=404, detail="Items not found")
    return items


@router.post('/add_item/')
def add_item(
    item: BaseMarketplaceItem,
    user: BaseUser,
):
    if user.admin_role:   
        item_id = MarketDatabaseAdapter.create_item(item_model=item)
        return {f"new item created with id: {item_id}"}

    return {"no permission to add items"}


@router.get('/get_item_by_id/', status_code=200)
def get_item_by_id(item_id: int):
    item = MarketDatabaseAdapter.get_item_by_id(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete('/delete_item_by_id/', status_code=200)
def delete_item_by_id(
    item_id: int, 
    user: BaseUser,
):
    if user.admin_role:
        MarketDatabaseAdapter.delete_item(item_id=item_id)
        return {"item deleted"}
    return {"no permission to delete items"}


