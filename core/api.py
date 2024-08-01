from fastapi import APIRouter, HTTPException, Depends, requests
# from fastapi.encoders import jsonable_encoder
from core.db import db
from core import tool
from bson.objectid import ObjectId


router = APIRouter()


@router.get("/api/get_juqin")
async def 获取剧情(id: str | None = None) -> dict | list | None:
    if id:
        ret_data = await db.jqdata.find_one({"_id": ObjectId(id)}, {"_id": 0})
    else:
        ret_data = await db.jqdata.find({}, {"data": 0}).to_list(length=100)
    ret_data = tool.encode_db_data(ret_data)
    return ret_data


@router.post("/api/save_juqin")
async def 保存剧情(name: str, data: dict) -> dict:
    print(data)
    db_return_data = await db.jqdata.insert_one({
        "name": name,
        "data": data
    })

    return {"id": str(db_return_data.inserted_id)}
