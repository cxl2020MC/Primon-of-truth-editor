from typing import Union
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import os

from app import tool, login


app = FastAPI()

app.include_router(login.router)


@app.get("/api")
async def read_root():
    return {"status": "200"}


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return_data = tool.return_data.update(
        {
            "status": exc.status_code,
            "msg": exc.detail
        }
    )
    return JSONResponse(
        status_code=exc.status_code,
        content=return_data,
    )
