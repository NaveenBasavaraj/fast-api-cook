from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
# model is used to validate data
# using base model


class UserPostIn(BaseModel):
    """ """

    body: str


class UserPost(UserPostIn):
    id: int


post_table = {}


@app.get("/get_post", response_model=list[UserPost])
async def get_all_posts():
    return list(post_table.values())


@app.post("/add_post", response_model=UserPostIn)
async def create_post(mathukathe_post: UserPostIn):
    # post.body -> json payload
    data = mathukathe_post.dict()
    last_record_id = len(post_table)
    new_post = {**data, "id": last_record_id}
    post_table[last_record_id] = new_post
    return new_post
