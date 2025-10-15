from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> str:
    """
    greetings
    """
    return {"message": "Hello World!"}


@app.get("/post")
async def add_post() -> str:
    return
