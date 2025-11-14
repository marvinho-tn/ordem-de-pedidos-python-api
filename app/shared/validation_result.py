from dataclasses import dataclass
from typing import List


@dataclass
class ValidationResult:
    def __init__(self, code: int, field: str):
        self.message = self.ERROR_MESSAGES.get(code, 'erro desconhecido')
        self.field = field
        self.code = code

    ERROR_MESSAGES = {
        422001: 'o request não pode ser nulo ou vazio.',

        422002: 'o nome não pode ser nulo ou vazio.',

        422003: 'o email não pode ser nulo ou vazio.',
        422004: 'é preciso inserir um email válido.',
        422005: 'já existe um usuário com esse email.',

        422006: 'a senha não pode ser nulo ou vazio.',
        422007: 'a senha deve conter um caracter maiúsculo, um minúsculo, um número, um especial e no mínimo 8 dígitos.',

        422008: 'user id não pode ser nulo.',
        422009: 'user id é inválido.',

        422010: 'o valor total não pode ser menor que zero.',

        422011: 'id não pode ser nulo.',
        422012: 'id é inválido.',

        404001: 'user id não encontrado.',
        404002: 'user email não encontrado.',
        404003: 'id não encontrado.',
    }


class ValidationResultList:
    def __init__(self):
        self.validations: List['ValidationResult'] = []
        self.result: object | None = None

    def add_error(self, field: str, code: int):
        self.validations.append(ValidationResult(code=code, field=field))

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
    
    def get_http_status(self) -> int:
        if self.is_valid():
            return 200

        codes = [int(str(v.code)[:3]) for v in self.validations]

        if 404 in codes:
            return 404
        if all(c == 422 for c in codes):
            return 422

        return codes[0]