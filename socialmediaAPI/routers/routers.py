from fastapi import APIRouter  # , HTTPException

# from fastapi.params import Body
from socialmediaAPI.models.models import Post

router = APIRouter()


@router.get("/")  # get is the method, "/" is the path operation
async def root():
    return {"message": "Social Media API"}


@router.get("/posts")
async def get_posts():
    return {"message": "these are all the posts"}


# @router.post("/createposts")
# async def create_post(payload: Post):  # payload: dict = Body(...)
#     return {
#         "message": "successfully created a post",
#         "new_post": f"title: {payload['title']}, content:{payload['content']}",
#     }


@router.post("/createposts")
async def create_post(new_posts: Post):  # payload: dict = Body(...)
    return new_posts
