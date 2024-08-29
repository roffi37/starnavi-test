from fastapi import HTTPException


sign_in_error = HTTPException(status_code=401, detail="Incorrect email or password")

invalid_signature_error = HTTPException(status_code=401, detail="Invalid JWT token")

relation_not_found = HTTPException(status_code=404, detail="Relation not found")
