from jose import JWTError, jwt
from fastapi import HTTPException
from datetime import datetime, timedelta
import os

# 设置签名密钥
签名密钥 = os.getenv("JWT_SECRET", "secret")
# 设置算法
加密算法 = "HS256"
# 单位分钟
登录令牌失效时间 = 60*24*30*3

def 生成登录令牌(data: dict) -> str:
    # 复制data字典
    to_encode = data.copy()
    # 设置过期时间
    expire = datetime.utcnow() + timedelta(minutes=登录令牌失效时间)
    # 更新过期时间
    to_encode.update({"exp": expire})
    # 编码jwt
    encoded_jwt = jwt.encode(to_encode, 签名密钥, algorithm=加密算法)
    # 返回编码后的jwt
    return encoded_jwt

def 验证登录令牌(token: str) -> dict:
    try:
        jwt_data = jwt.decode(token, 签名密钥, algorithms=[加密算法])
        # username: str = jwt_data.get("sub")
        return jwt_data
    except JWTError:
        raise HTTPException(status_code=403, detail="无效的token")
