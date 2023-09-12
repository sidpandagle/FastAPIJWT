from fastapi import FastAPI
from todo import todo_router
from user import user_router

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}


app.include_router(todo_router)
app.include_router(user_router)
