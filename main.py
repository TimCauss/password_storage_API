from fastapi import FastAPI
# from models import root_model

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


