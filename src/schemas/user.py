from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class UserSignInSchema(BaseModel):
    email: EmailStr
    password: str


class UserCreateSchema(UserSignInSchema):
    username: str


class UserSchema(UserCreateSchema):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
