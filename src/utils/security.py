import bcrypt


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    bytes_password = password.encode()
    return bcrypt.hashpw(bytes_password, salt)

def validate_password(password: str, hashed_password: bytes) -> bool:
    password = password.encode()
    return bcrypt.checkpw(password, hashed_password)
