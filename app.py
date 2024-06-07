from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
# from pydantic import BaseModel
from typing import List
from core import tool

app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    retdeta = tool.return_data

    return retdeta.update(status=exc.status_code, msg=exc.detail)
    

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
