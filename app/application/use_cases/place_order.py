from dataclasses import dataclass
from datetime import datetime, timezone
import uuid

from error_codes import INVALID_USER_ID, REQUEST_NULL, USER_ID_NOT_FOUND, USER_ID_NULL, VALUE_CANNOT_BE_LESS_THAN_ZERO
from domain.models.order import Order
from domain.repositories.order_repository import OrderRepository
from domain.repositories.user_repository import UserRepository
from domain.value_objects.order_status import OrderStatus
from infrastructure.publishers.order_publisher import publish_order
from shared.uuid_utils import is_valid_uuid4
from shared.validation_result import ValidationResultList


@dataclass
class PlaceOrderInput:
    user_id: str
    total_amount: float

@dataclass
class PlaceOrderOutput:
    id: str

class PlaceOrderUseCase:
    def __init__(
            self, 
            user_repository: UserRepository,
            order_repository: OrderRepository
        ):
        self.user_repository = user_repository
        self.order_repository = order_repository

    def execute(self, input: PlaceOrderInput) -> ValidationResultList:
        validation_result = ValidationResultList()

        if input is None:
            validation_result.add_error('input', REQUEST_NULL)
            return validation_result

        if input.user_id is None:
            validation_result.add_error('input.user_id', USER_ID_NULL)

        user_id = None

        if is_valid_uuid4(input.user_id):
            user_id = uuid.UUID(input.user_id, version=4)
        else:
            validation_result.add_error('input.user_id', INVALID_USER_ID)

        if user_id:
            user = self.user_repository.get_by_id(user_id)
            if user is None:
                validation_result.add_error('input.user_id', USER_ID_NOT_FOUND)

        if input.total_amount < 0:
            validation_result.add_error('input.total_amount', VALUE_CANNOT_BE_LESS_THAN_ZERO)

        if validation_result.is_valid() is False:
            return validation_result

        order = Order(
            user_id=user.id,
            status=OrderStatus.PENDING.value,
            total_amount=input.total_amount,
            created_at=datetime.now(timezone.utc)
        )
        
        self.order_repository.add(order)

        publish_order(order, user)

        output = PlaceOrderOutput(id=str(order.id))
        validation_result.set_result(output)

        return validation_result