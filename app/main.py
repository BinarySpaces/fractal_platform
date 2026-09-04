from fastapi import FastAPI

from app.routers import router

app = FastAPI(title='Fractal Generator API', version='0.1.0')

app.include_router(router)


@app.get('/')
async def root():
    return {'message': 'Fractal API is running!'}
