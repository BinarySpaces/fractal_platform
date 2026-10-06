from datetime import datetime

from pydantic import BaseModel, ConfigDict


class FractalResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    fractal_name: str
    scheme: str | None
    image_url: str
    created_at: datetime
