from fastapi import (
    APIRouter,
    Depends,
    status,
    Request,
    HTTPException
)

from database.models import BaseUser
from user.base_adapter import UserDatabaseAdapter
from crypto.instructions import create_wallet

router = APIRouter(prefix='/users', tags=['users'])


@router.post('/create_user/', status_code=201)
def create_user(user: BaseUser):
    user.public_key, user.private_key = create_wallet()
    user_id = UserDatabaseAdapter.create_user(user_model=user)
    return {f"new user created with id: {user_id}"}


@router.get('/get_user_by_id/', status_code=200)
def get_user_by_id(user_id: int):
    user = UserDatabaseAdapter.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get('/get_users_list/', status_code=200)
def get_users_list(left: int, right: int):
    users_list = UserDatabaseAdapter.get_users_list(left=left, right=right)
    return users_list


@router.delete('/delete_user_by_id/', status_code=200)
def delete_user_by_id(user_id: int):
    UserDatabaseAdapter.delete_user(user_id=user_id)
    return {"user deleted"}


@router.post('/user/add_event')
def add_event_to_user(user_id: int):
    UserDatabaseAdapter.add_event(user_id=user_id)
