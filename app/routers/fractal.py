from fastapi import APIRouter

from app.models.base_params import BaseParams
from app.services import FractalService

router = APIRouter(prefix='/fractal', tags=['fractal'])

@router.post('/generate')
async def generate_fractal(params: BaseParams):
    return await FractalService.generate_random_fractal(params)
