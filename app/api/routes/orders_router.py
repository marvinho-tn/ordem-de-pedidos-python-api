from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from application.use_cases.place_order import PlaceOrderUseCase, PlaceOrderInput
from application.use_cases.update_order_status import UpdateOrderStatusUseCase
from infrastructure.config.db import get_db
from infrastructure.repositories.order_repository import PostgresOrderRepository
from infrastructure.repositories.user_repository import PostgresUserRepository


router = APIRouter()

@router.post('/', response_model=dict)
def place_order(input: PlaceOrderInput, db: Session = Depends(get_db)):
    order_repo = PostgresOrderRepository(db)
    user_repo = PostgresUserRepository(db)
    usecase = PlaceOrderUseCase(user_repository=user_repo, order_repository=order_repo)

    result = usecase.execute(input)

    return result.to_dict()

@router.get('/{id}/update-status', response_model=dict)
def update_status(id: str, db: Session = Depends(get_db)):
    order_repo = PostgresOrderRepository(db)
    usecase = UpdateOrderStatusUseCase(order_repository=order_repo)
    
    result = usecase.execute(id)

    return result.to_dict()
