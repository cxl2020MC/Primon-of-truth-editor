from fastapi import APIRouter, HTTPException, Depends, requests
# from fastapi.encoders import jsonable_encoder
from core.db import db
from core import tool
from bson.objectid import ObjectId
# from typing import Union

# import traceback


router = APIRouter()


@router.get("/api/get_juqin")
async def 获取剧情(id: str = "") -> dict | list | None:
    if id: 
        ret_data = await db.jqdata.find_one({"_id": ObjectId(id)}, {"_id": 0})
    else:
        ret_data = await db.jqdata.find({}).to_list(length=100)
    ret_data = tool.encode_db_data(ret_data)
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
