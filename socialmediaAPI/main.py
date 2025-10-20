from fastapi import FastAPI

from socialmediaAPI.routers.routers import router

# from fastapi.params import Body

app = FastAPI()

app.include_router(router)


# @app.get("/")  # get is the method, "/" is the path operation
# async def root():
#     return {"message": "Social Media API"}


# @app.get("/posts")
# async def get_posts():
#     return {"message": "these are all the posts"}


# @app.post("/createposts")
# async def create_post(payload: Post):  # payload: dict = Body(...)
#     return {
#         "message": "successfully created a post",
#         "new_post": f"title: {payload['title']}, content:{payload['content']}",
#     }
