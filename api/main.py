# from typing import Union
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app import tool, login, api


app = FastAPI()

app.include_router(login.router)
app.include_router(api.router)


@app.get("/api")
async def read_root():
    return {"code": "200"}


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return_data = tool.return_data.copy()
    return_data.update(
        {
            "code": exc.status_code,
            "msg": str(exc)
        }
    )
    return JSONResponse(
        status_code=exc.status_code,
        content=return_data,
    )


@app.exception_handler(Exception)
async def unicorn_exception_handler(request, exc):
    return_data = tool.return_data.copy()
    return_data.update(
        {
            "code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "msg": f"服务器错误: {exc}"
        }
    )
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=return_data,
    )
