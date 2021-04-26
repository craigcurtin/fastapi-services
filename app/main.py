from utils.app_exceptions import AppExceptionCase
from utils.setup_logger import setup_logger
from fastapi import FastAPI

from routers import foo
from config.database import create_tables

from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

import uvicorn
import logging

from utils.request_exceptions import (
    http_exception_handler,
    request_validation_exception_handler,
)
from utils.app_exceptions import app_exception_handler

create_tables()


app = FastAPI()


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, e):
    return await http_exception_handler(request, e)


@app.exception_handler(RequestValidationError)
async def custom_validation_exception_handler(request, e):
    return await request_validation_exception_handler(request, e)


@app.exception_handler(AppExceptionCase)
async def custom_app_exception_handler(request, e):
    return await app_exception_handler(request, e)


app.include_router(foo.router)


@app.get("/")
async def root():
    return {"message": "Hello from FastAPI"}

if __name__ == "__main__":
    #    uvicorn.run(app, host="0.0.0.0", port=7000, log-level=logging.DEBUG)
    setup_logger('report_service', logging.DEBUG)
    logging.info("Web Server starting up ...")
    uvicorn.run(app, host="0.0.0.0",
                port=7000,
                log_level=logging.DEBUG,
                debug=True,
                # reload=True,
    )
