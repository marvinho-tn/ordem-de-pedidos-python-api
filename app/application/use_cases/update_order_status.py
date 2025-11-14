from dataclasses import dataclass
import uuid

from application.errror_codes import ID_NOT_FOUND, INVALID_ID, ID_NULL
from domain.repositories.order_repository import OrderRepository
from domain.value_objects.order_status import OrderStatus
from shared.uuid_utils import is_valid_uuid4
from shared.validation_result import ValidationResultList


@dataclass
class UpdateOrderStatusOutput:
    status: str

class UpdateOrderStatusUseCase:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def execute(self, id: str) -> ValidationResultList:
        validation_result = ValidationResultList()

        if id is None:
            validation_result.add_error('id', ID_NULL)
            return validation_result

        if not is_valid_uuid4(id):
            validation_result.add_error('id', INVALID_ID)
            return validation_result

        order_id = uuid.UUID(id, version=4)
        order = self.order_repository.get_by_id(order_id)

        if order is None:
            validation_result.add_error('id', ID_NOT_FOUND)
            return validation_result

        order.status = self.to_next_status(order.status)
        self.order_repository.update_order(order)

        output = UpdateOrderStatusOutput(status=order.status)
        validation_result.set_result(output)

        return validation_result


    def to_next_status(self, status: str) -> OrderStatus:
        if status == OrderStatus.PENDING.value:
            return OrderStatus.WAITING_PAYMENT.value
        if status == OrderStatus.WAITING_PAYMENT.value:
            return OrderStatus.PAID.value
        