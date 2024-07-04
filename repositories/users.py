from typing import List

from schemas.users import UserVip, UserMulti

from datetime import datetime

class UserRepository:
    
    def get_vip_users(self) -> List[UserVip]:
        return [UserVip(user_id='0000001', vip_level='1', start_date=datetime.strptime('30-01-12', '%d-%m-%y').date(), until_date=datetime.strptime('30-01-12', '%d-%m-%y').date())]
    
    def get_multi_users(self) -> List[UserMulti]:
        return [UserMulti(user_id='0000001', instagram_accounts='{asdasdasd, asdasdasd}')]