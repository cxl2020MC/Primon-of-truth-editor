from fastapi import APIRouter, HTTPException, Depends, requests
from app.db import db
from app import tool
from typing import Union

router = APIRouter()


@router.get("/api/get_juqin")
async def 获取剧情():
    ret_deta = tool.return_data.copy()
    juqinnames = db.jqnames.find({})
    jqnamedata = await juqinnames.to_list(length=100)
    ret_deta.update({"data": jqnamedata})
    print(ret_deta)
    return ret_deta


@router.post("/api/save_juqin")
async def 保存剧情(name: str, data: dict):
    print(data)
    if name:
        await db.jqnames.insert_one({"name": name})
        await db.jqdata.insert_one({
            "name": name,
            "data": data
        })
    return tool.return_data
