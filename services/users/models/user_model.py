from pydantic import BaseModel, UUID4
from typing import Optional


class UserModel(BaseModel):
    email: str
    name: str
    nickname: str
    avatar_url: Optional[str] = None
    uuid: UUID4
