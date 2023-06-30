import asyncio
import sys
import uvicorn
from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from loguru import logger
from app_api.reports.routes import reports_app

logger.add("./logs/info.log", rotation="500 MB", level="INFO")
logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")
app = FastAPI(title="Skynet API", description="", version="1.0.0")
app.include_router(reports_app, prefix="/api")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(GZipMiddleware, minimum_size=10000000)  # Approximately 10 MB


management_api = FastAPI(title="Skynet Management API", version="1.0.0")




if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info", reload=True, proxy_headers=True, lifespan="on")
