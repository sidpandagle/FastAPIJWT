import time
from datetime import datetime
from fastapi import HTTPException, status
from jose import jwt, JWTError


def create_user_token(user: str) -> str:
    payload = {"user": user, "expires": time.time() + 3600}
    token = jwt.encode(payload, "HI5HL3V3L$3CR3T", algorithm="HS256")
    return token


def verify_access_token(token: str) -> dict:
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoidGVzdCIsImV4cGlyZXMiOjE2OTQ1MDM3MTMuNzQ0OTY4N30.jUGU1dDvDwKqWBm-WaTHWIMBzKk7tpCZ7VoYv-mph6w"
    try:
        data = jwt.decode(token, "HI5HL3V3L$3CR3T", algorithms=["HS256"])
        expire = data.get("expires")
        if expire is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No access token supplied",
            )
        if datetime.utcnow() > datetime.utcfromtimestamp(expire):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Token expired!",
            )
        return data
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid Token",
        )
