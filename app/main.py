from fastapi import FastAPI

from api.routes.orders_router import router as orders_router
from api.routes.users_router import router as users_router


app = FastAPI()

app.include_router(orders_router, prefix='/orders', tags=['orders'])
app.include_router(users_router, prefix='/users', tags=['users'])