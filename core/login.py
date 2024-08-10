from fastapi import APIRouter, HTTPException, status, Depends, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from pydantic import BaseModel
import os
import json
from . import tool, login_tool

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/login")

class User(BaseModel):
    username: str
    password: str

@router.post("/api/login")
async def login(re_userdata: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """登录接口"""
    alluserdata = json.loads(os.getenv("ADMIN_USERDATA", "{}"))
    userdata = {
        "username": re_userdata.username,
        "password": re_userdata.password,
        "admin": True,
    }
    if not userdata in alluserdata:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
        )
    jwt_data = {
        "username": re_userdata.username,
        "admin": True,
        # "password": re_userdata.password
    }
    access_token = login_tool.生成登录令牌(data=userdata)
    return_data = tool.return_data.copy()
    return_data.update(
        {
            "status": 200,
            "msg": "登录成功",
            "access_token": access_token,
            "token_type": "bearer"
        }
    )
    return return_data


@router.get("/api/check_login")
async def check_login(token: str = Depends(oauth2_scheme)):
    return login_tool.验证登录令牌(token)
