
from fastapi import HTTPException
from app.schemes.auth_scheme import AuthCreate, AuthLogin, AuthPublic


""" 회원 가입 """
def sign_up_process(auth: AuthCreate):

    return AuthPublic(
        id = auth.id,
        name = "이말숙"
    )


""" 회원 로그인 """
def sign_in_process(auth: AuthLogin):
    if(auth.id == "id01" and auth.pwd == "pwd01"):
        return AuthPublic(
            id = auth.id,
            name = "이말숙"
        )
    else:
        raise HTTPException(
            status_code = 401,
            detail = "아이디 또는 패스워드가 올바르지 않습니다."      
        )


""" 회원 로그아웃 """
def sign_out_process(input_id: str):

        return AuthPublic(
            id = input_id,
        )
