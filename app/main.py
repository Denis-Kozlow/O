from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from app.db import create_tables, delete_tables
from app.schemas import SDepAdd
from app.repository import DepRepository
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield
    await delete_tables()


app = FastAPI(lifespan=lifespan)


@app.post("/depos")
async def add_dep(dep: SDepAdd = Depends()) -> dict:
    resp = await DepRepository.add_dep(dep)
    return resp
if __name__ == '__main__':
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
