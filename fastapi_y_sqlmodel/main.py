from fastapi import Depends, FastAPI
from fastapi.concurrency import asynccontextmanager

from src.database.database import create_db_and_tables, engine
from src.routers import hero_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Inicializar la base de datos
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(hero_router.router)
