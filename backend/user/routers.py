from fastapi import (
    APIRouter,
    Depends,
    status,
    Request,
    HTTPException
)



router = APIRouter(
    prefix='/users',
    tags=['users'],
)

@router.get('/get_current_user/')
def get_user():
    return 'test user'