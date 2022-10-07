from fastapi import (
    APIRouter,
    Depends,
    status,
    Request,
    HTTPException
)

from database.models import BaseUser
from user.base_adapter import UserDatabaseAdapter

router = APIRouter(
    prefix='/events', tags=['events']
)


@router.post('/create_post/', status_code=201)
def create_post():
    return 'test'


@router.put('/update_post/', status_code=201)
def update_post():
    return 'test'


@router.delete('/delete_post/', status_code=201)
def delete_post(post_id: int):
    return 'test'
