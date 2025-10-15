from fastapi import APIRouter

from mathukathe.models.post_models import UserPost, UserPostIn

router = APIRouter()


post_table = {}


@router.get("/get_post", response_model=list[UserPost])
async def get_all_posts():
    return list(post_table.values())


@router.post("/add_post", response_model=UserPostIn)
async def create_post(mathukathe_post: UserPostIn):
    # post.body -> json payload
    data = mathukathe_post.dict()
    last_record_id = len(post_table)
    new_post = {**data, "id": last_record_id}
    post_table[last_record_id] = new_post
    return new_post
