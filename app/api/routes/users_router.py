from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from application.use_cases.create_user import CreateUserUseCase, CreateUserInput
from application.use_cases.get_user_by_email import GetUserByEmailUseCase
from infrastructure.config.db import get_db
from infrastructure.repositories.user_repository import PostgresUserRepository


router = APIRouter()

@router.post('/', response_model=dict)
def create_user(input: CreateUserInput, db: Session = Depends(get_db)):
    user_repo = PostgresUserRepository(db)
    usecase = CreateUserUseCase(user_repository=user_repo)

    result = usecase.execute(input)

    return result.to_dict()

@router.get('/:email', response_model=dict)
def get_by_email(email: str, db: Session = Depends(get_db)):
    user_repo = PostgresUserRepository(db)
    usecase = GetUserByEmailUseCase(user_repository=user_repo)

    result = usecase.execute(email)

    return result.to_dict()
