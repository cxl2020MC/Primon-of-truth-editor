from typing import Union
from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/api/")
def read_root():
    return {"status": "200"}


@app.post("/api/login/")
def login():
    
    return {"status": "200"}

@app.post("/api/item/")
def create_item(
    item: Annotated[
        Union[str, None],
        Depends(oauth2_scheme)
    ]
):
    return {"item": item}