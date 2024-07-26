from bson import ObjectId
from typing import Any
# from typing import Dict

    
return_data = {
    "status": 200,
    "msg": "OK",
    "data": None
}

# 将ObjectId转换为字符串
def encode_db_data(data: dict | list | None) ->dict | list | None:
    # data = dict(data)
    if isinstance(data, list):
        for item in data:
            encode_db_data(item)
    elif isinstance(data, dict):
        data["_id"] = str(data["_id"])
    return data
