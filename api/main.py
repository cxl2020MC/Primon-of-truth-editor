from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/api/")
def read_root():
    return {"status": "200"}


@app.get("/api/login/")
def read_item():
    return {"status": "200"}