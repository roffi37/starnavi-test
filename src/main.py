from fastapi import FastAPI

from src.routers import user
from src.routers import post

app = FastAPI()


@app.get("/")
def main():
    return {"Hello": "World"}

app.include_router(user.router)
app.include_router(post.router)
