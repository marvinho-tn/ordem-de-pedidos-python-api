from dataclasses import dataclass
from datetime import datetime, timezone

from application.errror_codes import EMAIL_NULL, EXISTANT_EMAIL, INVALID_EMAIL, INVALID_PASSWORD, PASSWORD_NULL, NAME_NULL, REQUEST_NULL
from domain.models.user import User
from domain.repositories.user_repository import UserRepository
from shared.email_utils import is_valid_email
from shared.password_utils import hash_password, is_valid_password
from shared.validation_result import ValidationResultList


@dataclass
class CreateUserInput:
    name: str
    email: str
    password: str

@dataclass
class CreateUserOutput:
    id: str

class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, input: CreateUserInput) -> ValidationResultList:
        validation_result = ValidationResultList()

        if input is None:
            validation_result.add_error('input', REQUEST_NULL)
            return validation_result
        
        if input.name is None or input.name.strip() is '':
            validation_result.add_error('input.name', NAME_NULL)
        
        if input.email is None or input.email.strip() is '':
            validation_result.add_error('input.email', EMAIL_NULL)

        if is_valid_email(input.email) is False:
            validation_result.add_error('input.email', INVALID_EMAIL)
        
        user = self.user_repository.get_by_email(input.email)

        if user is not None:
            validation_result.add_error('input.email', EXISTANT_EMAIL)

        if input.password is None or input.password.strip() is '':
            validation_result.add_error('input.password', PASSWORD_NULL)

        if is_valid_password(input.password) is False:
            validation_result.add_error('input.password', INVALID_PASSWORD)

        if not validation_result.is_valid():
            return validation_result

        user = User(
            name=input.name,
            email=input.email,
            password_hash=hash_password(input.password),
            created_at=datetime.now(timezone.utc))
        
        self.user_repository.add(user)

        output = CreateUserOutput(id=str(user.id))
        validation_result.set_result(output)

        return validation_result
