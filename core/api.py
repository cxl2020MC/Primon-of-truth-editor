from fastapi import APIRouter, HTTPException, Depends, requests
# from fastapi.encoders import jsonable_encoder
from core.db import db
from core import tool
from typing import Union

import traceback

from pydantic import BaseModel
from bson import ObjectId
BaseModel.model_config["json_encoders"] = {ObjectId: lambda v: str(v)}

router = APIRouter()


@router.get("/api/get_juqin")
async def 获取剧情():
    ret_deta = tool.return_data.copy()
    try:
        jqnamedata = list(db.jqnames.find({}, {"_id": 0}))
        ret_deta.update({"data": jqnamedata})
    except:
        ret_deta.update({"code": 1, "msg": traceback.format_exc()})
    print(ret_deta)
    return ret_deta


@router.post("/api/save_juqin")
async def 保存剧情(name: str, data: dict):
    print(data)
    # await db.jqnames.insert_one({"name": name})
    return_data = await db.jqdata.insert_one({
        "name": name,
        "data": data
    })
    
    
    return tool.return_data
