# auth_scheme.py

from pydantic import BaseModel, Field

# 회원가입
class AuthCreate(BaseModel):
    id:str
    pwd:str
    name:str

# 로그인
class AuthLogin(BaseModel):
    id:str
    pwd:str

# 밖으로 전송할 내용
class AuthPublic(BaseModel):
    id:str
    name:str | None = None