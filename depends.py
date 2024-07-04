from repositories.users import UserRepository
from services.users import UserService

"""
Файл внедрения зависимостей
"""

# repository - работа с БД

user_repository = UserRepository()

# service - слой UseCase
user_service = UserService(user_repository)

def get_user_service() -> UserService:
   return user_service