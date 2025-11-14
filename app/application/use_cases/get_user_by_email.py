from dataclasses import dataclass

from application.errror_codes import EMAIL_NULL, INVALID_EMAIL, NAME_NULL, USER_EMAIL_NOT_FOUND
from domain.repositories.user_repository import UserRepository
from shared.email_utils import is_valid_email
from shared.validation_result import ValidationResultList


@dataclass
class GetUserByEmailOutput:
    id: str
    name: str
    email: str

class GetUserByEmailUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, email: str) -> ValidationResultList:
        validation_result = ValidationResultList()
        
        if email is None or email.strip() is '':
            validation_result.add_error('email', EMAIL_NULL)

        if is_valid_email(email) is False:
            validation_result.add_error('email', INVALID_EMAIL)
        
        user = self.user_repository.get_by_email(email)

        if user is None:
            validation_result.add_error('email', USER_EMAIL_NOT_FOUND)
            return validation_result

        output = GetUserByEmailOutput(
            id=user.id,
            name=user.name,
            email=user.email)

        validation_result.set_result(output)

        return validation_result
        
