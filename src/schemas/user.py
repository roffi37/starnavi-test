from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreateSchema(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserSchema(UserCreateSchema):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
