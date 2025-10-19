from fastapi import APIRouter, HTTPException

from mathukathe.models.post_models import (
    Comment,
    CommentIn,
    UserPost,
    UserPostIn,
    UserPostWithComments,
)

router = APIRouter()


post_table = {}
comment_table = {}


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


@router.get("/get_comments", response_model=list[UserPost])
async def get_all_comments():
    return list(comment_table.values())


def find_post(post_id: int):
    return post_table.get(post_id)


@router.post("/add_comment", response_model=Comment)
async def create_comment(comment: CommentIn):
    # post.body -> json payload
    post = find_post(comment.post_id)
    if not post:
        raise HTTPException(status_code=404, detail="")
    data = comment.dict()
    last_record_id = len(comment_table)
    new_comment = {**data, "id": last_record_id}
    comment_table[last_record_id] = new_comment
    return new_comment


@router.get("/post/{post_id}/comment", response_model=list[Comment])
async def get_comments_on_the_post(post_id: int):
    return [
        comment for comment in comment_table.values() if comment["post_id"] == post_id
    ]


@router.get("/post/{post_id}", response_model=UserPostWithComments)
async def get_post_with_comments(post_id: int):
    post = find_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="")

    return {"post": post, "comments": await get_comments_on_the_post(post_id)}
