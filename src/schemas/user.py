from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    uuid: str
    email: EmailStr
    username: str
    password: str
    created_at: datetime
