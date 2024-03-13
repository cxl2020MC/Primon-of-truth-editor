from fastapi import APIRouter, HTTPException, Depends, requests
from app.db import db
from app import tool

router = APIRouter()


@router.get("/api/get_juqin")
async def 获取剧情():
    ret_deta = tool.return_data.copy()
    ret_deta.update({"data": db.juqin.find()})
    print(ret_deta)
    return ret_deta
