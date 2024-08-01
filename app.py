from core import tool, login, api, page
from core.log import logger as log
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import traceback
import dotenv

dotenv.load_dotenv()


app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

app.include_router(page.router)
app.include_router(login.router)
app.include_router(api.router)


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    ret_data = tool.return_data.copy()

    ret_data.update({"msg": exc.detail})
    return JSONResponse(ret_data, status_code=exc.status_code)

@app.exception_handler(Exception)
async def exception_handler(request, exc):
    ret_data = tool.return_data.copy()
    错误信息 = traceback.format_exc()
    log.error(错误信息)
    ret_data.update({"msg": f"服务器错误：{exc}", "traceback": 错误信息})
    
    return JSONResponse(ret_data, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
