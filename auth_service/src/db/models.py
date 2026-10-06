from datetime import datetime

from sqlalchemy import Boolean, DateTime, Index, String, func
from sqlalchemy.orm import Mapped, mapped_column

from src.db.base import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255))
    password_hash: Mapped[str] = mapped_column(String(255))
    is_premium: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    __table_args__ = (
        Index('ix_users_email_unique', 'email', unique=True),
    )
