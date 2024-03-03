from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import os, json
from . import tool, login_tool

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/login")



@router.post("/api/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    alluserdata = json.loads(os.getenv('LOGIN_USERDATA'))
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
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/api/get_userinfo")
async def login(token: str = Depends(oauth2_scheme)):
    return login_tool.验证登录令牌(token)