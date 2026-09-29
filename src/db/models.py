from datetime import datetime

from sqlalchemy import DateTime, Index, String, func
from sqlalchemy.orm import Mapped, mapped_column

from src.db.base import Base


class Fractal(Base):
    __tablename__ = 'fractals'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column()
    fractal_name: Mapped[str] = mapped_column(String(50))
    scheme: Mapped[str | None] = mapped_column(String(50), nullable=True)
    image_url: Mapped[str] = mapped_column(String(500))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    __table_args__ = (
        Index('ix_fractals_user_created', 'user_id', 'created_at'),
    )
