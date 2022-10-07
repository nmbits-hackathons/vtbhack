from fastapi import (
    APIRouter,
    Depends,
    status,
    Request,
    HTTPException
)

router = APIRouter(
    prefix='/marketplace',
    tags=['marketplace'],
)


@router.get('/marketplace/')
def get_market():
    return 'marketplace user'
