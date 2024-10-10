from typing import Optional, Literal
from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    age: Optional[int] = None


user = User(name="Ivan", age="30", City())
paylaod = user.json()