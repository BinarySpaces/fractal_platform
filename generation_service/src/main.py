from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.exc import DBAPIError

from src.db.redis_client import redis_client
from src.routers import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await redis_client.aclose()

app = FastAPI(title='Fractal Service', lifespan=lifespan)

# CORS — разрешаем фронту обращаться к бэку
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*'],
)

app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(router)

@app.exception_handler(DBAPIError)
async def db_error_handler(request: Request, exc: DBAPIError):
    return JSONResponse(
        status_code=503,
        content={'error': 'Database temporarily unavailable'},
    )

@app.get('/')
async def main():
    return {'status': 'ok'}
