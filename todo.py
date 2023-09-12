from typing import List, Optional
from fastapi import APIRouter, Path, Depends
from auth.authenticate import authenticate
from model import Todo, TodoItems

todo_router = APIRouter()
todo_list = []


@todo_router.post("/todo")
async def add_todo(todo: Todo, user: str = Depends(authenticate)) -> dict:
    todo_list.append(todo)
    return {"message": "Todo Added Successfully"}


@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todos() -> dict:
    return {"todos": todo_list}


@todo_router.get("/todo/{todo_id}", response_model=Todo)
async def get_todo_by_id(
    todo_id: int = Path(..., title="Getting Todo by Todo ID")
) -> dict:
    print(todo_id)
    for todo in todo_list:
        if todo_id == todo.id:
            return todo
    return None
