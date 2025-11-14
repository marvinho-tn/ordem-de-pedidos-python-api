from fastapi import FastAPI

import logging

from api.routes.orders_router import router as orders_router
from api.routes.users_router import router as users_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)

app = FastAPI()

app.include_router(orders_router, prefix='/orders', tags=['orders'])
app.include_router(users_router, prefix='/users', tags=['users'])