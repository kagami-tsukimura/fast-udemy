import asyncio

from sqlalchemy.ext.asyncio import create_async_engine

from models.contact import Base

DB_URL = "sqlite+aiosqlite:///fastapi-app.db"
engine = create_async_engine(DB_URL, echo=True)


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(main())
