from fastapi import FastAPI

from mathukathe.routers.post_routers import router as post_router

app = FastAPI()
app.include_router(post_router)
