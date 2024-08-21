import jwt
from datetime import datetime, UTC, timedelta

from src.config import get_settings


settings = get_settings()

def encode_jwt(
        payload: dict,
        expire_minutes: int,
        expired_time: timedelta | None = None,
) -> str:
    now = datetime.now(UTC)
    if expired_time:
        expire = now + expired_time
    else:
        expire = now + timedelta(minutes=expire_minutes)
    payload.update(
        exp=expire,
        iat=now,
    )
    encoded = jwt.encode(
        payload=payload,
        key=settings.jwt_settings.JWT_SECRET_KEY,
        algorithm=settings.jwt_settings.ALGORITHM,
    )
    return encoded


def decode_jwt(
        token: str,
) -> dict:
    decoded = jwt.decode(
        token=token,
        key=settings.jwt_settings.JWT_SECRET_KEY,
        algorithms=[settings.jwt_settings.JWT_ALGORITHM],
    )
    return decoded


def create_access_token(email: str) -> dict:
    payload: dict = {"sub": email}
    token = encode_jwt(payload, 5)
    return {"access_token": token, "token_type": "Bearer"}