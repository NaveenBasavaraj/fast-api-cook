from fastapi import FastAPI

app = FastAPI()


@app.get("/")  # get is the method, "/" is the path operation
async def root():
    return {"message": "Social Media API"}


@app.get("/posts")
async def get_posts():
    return {"message": "these are all the posts"}


@app.post("/createposts")
async def create_post():
    return {"message": "successfully created post"}
