from typing import List
from pydantic import BaseModel


class Item(BaseModel):
    item: str
    status: str


class Todo(BaseModel):
    id: int
    item: Item

class TodoItems(BaseModel):
    todos: List[Todo]
