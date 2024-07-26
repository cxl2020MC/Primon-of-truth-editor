from fastapi import APIRouter, HTTPException, Depends, requests
# from fastapi.encoders import jsonable_encoder
from core.db import db
from core import tool
from typing import Union

import traceback


router = APIRouter()


@router.get("/api/get_juqin")
async def 获取剧情():
    ret_data = await db.jqdata.find({}, {"_id": 0}).to_list(length=100)
    return ret_data


@router.post("/api/save_juqin")
async def 保存剧情(name: str, data: dict) -> dict:
    print(data)
    # ret_data = tool.return_data.copy()
    # await db.jqnames.insert_one({"name": name})
    db_return_data = await db.jqdata.insert_one({
        "name": name,
        "data": data
    })

    return {"id": str(db_return_data.inserted_id)}
