from fastapi import APIRouter, HTTPException, Depends, requests
from app.db import db

router = APIRouter()

@router.get("/api/get_juqin")
async def 获取剧情(requests):
    return db.juqin.find()