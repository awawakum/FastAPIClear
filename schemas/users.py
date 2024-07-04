from datetime import datetime
from pydantic import BaseModel


class UserVip(BaseModel):
    user_id: str
    vip_level: str
    start_date: datetime
    until_date: datetime


class UserMulti(BaseModel):
    user_id: str
    instagram_accounts: str