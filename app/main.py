from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

import logging

from api.routes.orders_router import router as orders_router
from api.routes.users_router import router as users_router
from error_codes import UNEXPECTED_ERROR
from shared.validation_result import ValidationResultList

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)

logger = logging.getLogger("main")

app = FastAPI()

app.include_router(orders_router, prefix='/orders', tags=['orders'])
app.include_router(users_router, prefix='/users', tags=['users'])

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.exception("Erro inesperado durante requisição", extra={"path": request.url.path})

    validation = ValidationResultList()
    validation.add_error(field="app", code=UNEXPECTED_ERROR)

    return JSONResponse(
        status_code=validation.get_http_status(),
        content=validation.to_dict()
    )