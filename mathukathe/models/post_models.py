from pydantic import BaseModel

# model is used to validate data
# using base model


class UserPostIn(BaseModel):
    """ """

    body: str


class UserPost(UserPostIn):
    id: int
