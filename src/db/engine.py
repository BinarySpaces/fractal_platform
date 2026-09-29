from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.config import settings

engine = create_async_engine(
    settings.database_url,
    echo=False,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,   # проверка соединения перед использованием
    pool_recycle=300,     # пересоздание каждые 5 минут
)

SessionLocal = async_sessionmaker(engine, expire_on_commit=False)
