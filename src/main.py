from fastapi import FastAPI

from src.routers import user

app = FastAPI()


@app.get("/")
def main():
    return {"Hello": "World"}

app.include_router(user.router)
