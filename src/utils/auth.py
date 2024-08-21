import jwt
from datetime import datetime, UTC, timedelta

from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt import InvalidSignatureError

from src.exceptions import invalid_signature_error
from src.config import get_settings


http_bearer = HTTPBearer()


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
        jwt=token,
        key=settings.jwt_settings.JWT_SECRET_KEY,
        algorithms=[settings.jwt_settings.ALGORITHM],
    )
    return decoded


def create_access_token(email: str) -> dict:
    payload: dict = {"sub": email}
    token = encode_jwt(payload, 5)
    return {"access_token": token, "token_type": "Bearer"}


def get_current_user(
        token: HTTPAuthorizationCredentials = Depends(http_bearer)
):
    try:
        payload = decode_jwt(token.credentials)
        if payload.get("sub"):
            return payload.get("sub")
    except InvalidSignatureError:
        raise invalid_signature_error
