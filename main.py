from fastapi import FastAPI
# from models import root_model

app = FastAPI()


@app.get("/")
async def index() -> bool:
    return True


@app.get('/creds')
async def read_creds():
    pass