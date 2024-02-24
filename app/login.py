from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
import os
from . import tool, login_tool

router = APIRouter()


@router.post("/api/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    alluserdata = os.getenv('LOGIN_USERDATA')
    userdata = {
        "username": form_data.username,
        "password": form_data.password
    }
    if not userdata in alluserdata:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Incorrect username or password"
        )

    return {"access_token": "OK", "token_type": "bearer"}
