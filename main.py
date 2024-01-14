from fastapi import FastAPI, Request
from Libs.logger import Logger
import time
import logging
import uuid

# from models import root_model

logger = Logger("req_logger")

app = FastAPI()

@app.middleware("http")
async def logs_requests(request: Request, call_next):
    #Adding ID for each request and IP source
    request_id = str(uuid.uuid4())
    source_ip = request.client.host
    start_time = time.time()
    
    response = await call_next(request)
    process_time = time.time() - start_time
    
    #logging informations
    logger.log(f'Request ID : {request_id} | Source IP : {source_ip} | Method: {request.method} | URL: {request.url} | Processing Time: {process_time} seconds.')
    
    return response


@app.get("/")
async def index() -> bool:
    return True