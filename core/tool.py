from bson import ObjectId
from typing import Any
# from typing import Dict

    
return_data = {
    "status": 200,
    "msg": "OK",
    "data": None
}

# 将ObjectId转换为字符串
def encode_db_data(data: Any) ->dict:
    data = dict(data)
    for key, value in data:
        if isinstance(value, ObjectId):
            data[key] = str(value)
    return data
