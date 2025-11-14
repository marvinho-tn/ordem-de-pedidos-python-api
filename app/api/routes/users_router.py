from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from application.use_cases.create_user import CreateUserUseCase, CreateUserInput
from application.use_cases.get_user_by_email import GetUserByEmailUseCase
from infrastructure.config.db import get_db
from infrastructure.repositories.user_repository import PostgresUserRepository


router = APIRouter()

@router.post('/', response_model=dict)  # depois você pode trocar para CreateUserOutput
def create_user(input: CreateUserInput, db: Session = Depends(get_db)):
    # cria os repositórios com a sessão do banco
    user_repo = PostgresUserRepository(db)

    # instancia o use case
    usecase = CreateUserUseCase(user_repository=user_repo)

    # executa
    result = usecase.execute(input)

    # retorna o objeto de sucesso ou erros
    return result.to_dict()  # supondo que ValidationResultList tenha um método para serializar

@router.get('/:email', response_model=dict)
def get_by_email(email: str, db: Session = Depends(get_db)):
    user_repo = PostgresUserRepository(db)
    usecase = GetUserByEmailUseCase(user_repository=user_repo)
    result = usecase.execute(email)

    return result.to_dict()
