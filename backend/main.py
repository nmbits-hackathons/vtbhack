from fastapi import FastAPI, Response, Request, APIRouter

import user.routers as user_routers
import events.routers as events_routers
import marketplace.routers as marketplace_routers
import uvicorn

import database.database_adapter

prefix_router = APIRouter(
    prefix='/api',
)

prefix_router.include_router(user_routers.router)
prefix_router.include_router(events_routers.router)
prefix_router.include_router(marketplace_routers.router)

app = FastAPI(title='VTB Hackaton MORE.Tech 4.0 API', docs_url='/')

app.include_router(prefix_router)

if __name__ == '__main__':
    uvicorn.run('__main__:app', host='127.0.0.1', port=8000, reload=True)
