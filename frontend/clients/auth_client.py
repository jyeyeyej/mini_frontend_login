from core.api_client import request

def login_process(id:str, pwd:str):
    return request("POST", f"/auth/sighin", json={"id":id, "pwd":pwd})


def logout_process(id:str):
    return request("GET", f"/auth/sighout/{id}")


def register_process(auth:dict):
    return request("POST", "/auth/create", json=auth)
