from fastapi import FastAPI, Depends

from contextlib import asynccontextmanager

from database import create_tables, delete_tables

from router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена!")
    await create_tables()
    print("База готова!")
    yield
    print("Выключение")
    # Clean up the ML models and release the resources


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)
