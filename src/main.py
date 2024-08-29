from fastapi import FastAPI

from src.routers import user
from src.routers import post
from src.routers import comment

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)
