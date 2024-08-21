from fastapi import HTTPException


sign_in_error = HTTPException(status_code=401, detail="Incorrect email or password")
