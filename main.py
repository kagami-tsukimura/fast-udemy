import uvicorn
from fastapi import FastAPI

from routers import contact

app = FastAPI()

app.include_router(contact.router)


@app.get("/")
async def example():
    """
    起動確認としてHello Worldを返します。
    """

    return {"message": "Hello World!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
