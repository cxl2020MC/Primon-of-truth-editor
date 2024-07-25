from core import tool, login, api, page
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
import traceback
import dotenv

dotenv.load_dotenv()


app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

app.include_router(page.router)
app.include_router(login.router)
app.include_router(api.router)


class ReturnData(BaseModel):
    status: int
    msg: str
    data: List[dict] = []

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    retdeta = tool.return_data.copy()

    retdeta.update({"status": exc.status_code, "msg": exc.detail})
    print(retdeta)

    return JSONResponse(retdeta, status_code=exc.status_code)


@app.exception_handler(Exception)
async def exception_handler(request, exc):
    retdeta = tool.return_data

    retdeta.update({"status": 500, "msg": traceback.format_exc()})

    return JSONResponse(retdeta, status_code=500)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
