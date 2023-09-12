from fastapi import APIRouter, Depends, Path
from fastapi.security import OAuth2PasswordRequestForm
from auth.hash_password import HashPassword
from auth.jwt_handler import verify_access_token, create_user_token

hp = HashPassword()

user_router = APIRouter()


@user_router.post("/signup/{email}/{password}")
async def signup(email: str, password: str) -> dict:
    password = "test123"
    hashed_password = hp.create_hash(password)
    return {"hashed_password": hashed_password}


@user_router.post("/signin")
async def signin(user: OAuth2PasswordRequestForm = Depends()) -> dict:
    password = "test123"
    if hp.verify_hash(
        password, "$2b$12$fAB/75enBaTakcHUb55WUucjURTONLuZGo2.YaR2N8lim8TKmbQRK"
    ):
        access_token = create_user_token(user.username)
        return {"access_token": access_token, "token_type": "Bearer"}
