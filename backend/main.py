from fastapi import FastAPI, Response, Request, APIRouter

import user.routers as user_routers
import marketplace.routers as marketplace_routers
import uvicorn


prefix_router = APIRouter(
    prefix='/api',
)
# prefix_router.include_router(network_auth_routers.router)  # oath2
# prefix_router.include_router(user_routers.router)
# prefix_router.include_router(post_routers.router)
#
# # prefix_router.include_router(vk_group_routers.router)  # VK
# prefix_router.include_router(bot_user_router.router)  # bot
# prefix_router.include_router(bot_post_router.router)  # bot
#
# prefix_router.include_router(user_routers.router)


prefix_router.include_router(user_routers.router)
prefix_router.include_router(marketplace_routers.router)


app = FastAPI(title='VTB Hackaton MORE.Tech 4.0 API',docs_url='/')

app.include_router(prefix_router)

if __name__ == '__main__':
    uvicorn.run('__main__:app', host='0.0.0.0', port=8000, reload=True)