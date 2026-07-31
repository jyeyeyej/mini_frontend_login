# product_router.py

from fastapi import APIRouter
from app.schemes.auth_scheme import (
    AuthLogin, AuthPublic, AuthCreate
)
from app.services.auth_service import (
    sign_up_process, sign_in_process, sign_out_process
)

auth_router = APIRouter(tags=["Auth"])

""" 회원 가입 """
@auth_router.post("/auth/create")
def create(auth:AuthCreate) -> AuthPublic:
    return sign_up_process(auth)

""" 회원 로그인 """
@auth_router.post("/auth/signin")
def signin(auth:AuthLogin) -> AuthPublic:
    return sign_in_process(auth)

""" 회원 로그아웃 """
@auth_router.get("/auth/signout/{input_id}")
def signout(input_id:str) -> AuthPublic:
    return sign_out_process(input_id)


