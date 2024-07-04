from typing import List

from repositories.users import UserRepository
from schemas.users import UserVip, UserMulti


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository
    
    def get_vip_users(self) -> List[UserVip]:
        vip_users = self.repository.get_vip_users()
        return vip_users
    
    def get_multi_users(self) -> List[UserMulti]:
        multi_users = self.repository.get_multi_users()
        return multi_users