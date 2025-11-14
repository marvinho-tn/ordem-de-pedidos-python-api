from dataclasses import dataclass
from typing import List


@dataclass
class ValidationResult:
    message: str
    field: str

    def __init__(self, message: str, field: str):
        self.message = message
        self.field = field

class ValidationResultList:
    def __init__(self):
        self.validations: List['ValidationResult'] = []
        self.result: object | None = None

    def add_error(self, field: str, message: str):
        self.validations.append(ValidationResult(message=message, field=field))

    def is_valid(self) -> bool:
        return len(self.validations) == 0

    def set_result(self, object: any):
        self.result = object

    def to_dict(self) -> dict:
        return {
            'is_valid': self.is_valid(),
            'validations': self.validations,
            'result': self.result.__dict__ if self.result else None
        }