from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import os
import json
from . import tool, login_tool

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/login")


@router.post("/api/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # alluserdata = json.loads(os.getenv('LOGIN_USERDATA'))
    alluserdata = [
        {
            "username": "admin",
            "password": "123456"
        }
    ]
    userdata = {
        "username": form_data.username,
        "password": form_data.password
    }
    if not userdata in alluserdata:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
        )
    access_token = login_tool.生成登录令牌(data=userdata)
    return_data = tool.return_data.copy()
    return_data.update(
        {
            "msg": "登录成功",
            "data": {
                "access_token": access_token,
                "token_type": "bearer"
            },
            # 兼容文档
            "access_token": access_token,
            "token_type": "bearer"
        }
    )
    return return_data


@router.get("/api/check_login")
async def check_login(token: str = Depends(oauth2_scheme)):
    return login_tool.验证登录令牌(token)
