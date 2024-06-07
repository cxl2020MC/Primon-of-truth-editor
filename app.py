from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
# from pydantic import BaseModel
from typing import List
import traceback

from core import tool, login, api


app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

app.include_router(login.router)
app.include_router(api.router)

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    retdeta = tool.return_data

    retdeta.update(status=exc.status_code, msg=traceback.format_exc())

    return retdeta
    

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
