from bson import ObjectId

    
return_data = {
    "status": 200,
    "msg": "OK",
    "data": None
}

# 将ObjectId转换为字符串
def encode_db_object_id(data: dict) ->dict:
    for key, value in data.items():
        if isinstance(value, ObjectId):
            data[key] = str(value)
    return data
