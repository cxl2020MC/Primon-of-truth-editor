# import motor.motor_asyncio
import pymongo
import os

数据库地址 = os.getenv("MONGODB_URL")
# client = motor.motor_asyncio.AsyncIOMotorClient(数据库地址)
client = pymongo.MongoClient(数据库地址)

db = client.tofe