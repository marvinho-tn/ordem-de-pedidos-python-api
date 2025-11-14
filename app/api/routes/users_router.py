from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from application.use_cases.create_user import CreateUserUseCase, CreateUserInput
from application.use_cases.get_user_by_email import GetUserByEmailUseCase
from infrastructure.config.db import get_db
from infrastructure.repositories.user_repository import PostgresUserRepository


router = APIRouter()

@router.post('/', response_model=dict)
def create_user(input: CreateUserInput, db: Session = Depends(get_db), response: Response = None):
    user_repo = PostgresUserRepository(db)
    usecase = CreateUserUseCase(user_repository=user_repo)

    result = usecase.execute(input)

    response.status_code = result.get_http_status()

    return result.to_dict()

@router.get('/:email', response_model=dict)
def get_by_email(email: str, db: Session = Depends(get_db), response: Response = None):
    user_repo = PostgresUserRepository(db)
    usecase = GetUserByEmailUseCase(user_repository=user_repo)

    result = usecase.execute(email)

    response.status_code = result.get_http_status()

    return result.to_dict()
