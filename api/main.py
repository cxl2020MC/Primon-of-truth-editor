from typing import Union
from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import os


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/login")


@app.get("/api")
def read_root():
    return {"status": "200"}


@app.post("/api/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = os.getenv('LOGIN_USER')
    if not username == form_data.username:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    password = os.getenv('LOGIN_PWD')
    if not password == form_data.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": "OK", "token_type": "bearer"}


@app.post("/api/item/")
def create_item(
    item: Union[str, None],
    token: str = Depends(oauth2_scheme)
):
    return {"item": item}
