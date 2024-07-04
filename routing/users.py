from typing import List

from fastapi import APIRouter, Depends

from depends import get_user_service
from schemas.users import UserVip, UserMulti
from services.users import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.get(
   "/multi",
   responses={400: {"description": "Bad request"}},
   response_model=List[UserMulti],
   description="Получение листинга multi пользователей",
)
async def get_multi_users(
       user_service: UserService = Depends(get_user_service),
) -> List[UserMulti]:
   users = user_service.get_multi_users()
   return users


@router.get(
   "/vip",
   responses={400: {"description": "Bad request"}},
   response_model=List[UserVip],
   description="Получение листинга vip пользователей",
)
async def get_vip_users(
       user_service: UserService = Depends(get_user_service),
) -> List[UserVip]:
   users = user_service.get_vip_users()
   return users