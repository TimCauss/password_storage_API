from fastapi import FastAPI, Request
from Libs.logger import Logger
import time
import logging
import uuid


logger = Logger("req_logger")
app = FastAPI()

@app.middleware("http")
async def logs_requests(request: Request, call_next):
    #Adding ID for each request and IP source
    start_time = time.time()
    request_id = str(uuid.uuid4())
    source_ip = request.client.host
    
    response = await call_next(request)
    process_time = time.time() - start_time
    
    logger.log(f'Request ID: {request_id} | Source IP : {source_ip} | Method: {request.method} | URL: {request.url} | time: {process_time}')

    return response


@app.get("/")
async def index() -> bool:
    time.sleep(5)
    return True