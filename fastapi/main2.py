from fastapi import FastAPI, Body, Response, status, HTTPException
from typing import Optional
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




class Todo(BaseModel):
    id: Optional[int]
    value: str


todo_list = []


@app.get("/todos")
async def get_todos():
    return todo_list


@app.post("/todos/create")
async def create_todo(data: Todo = Body()):
    new_todo = Todo(id=len(todo_list) + 1, value=data.value)
    todo_list.append(new_todo)
    print(new_todo)
    return new_todo


@app.patch("/todos")
async def update_todo(data: Todo = Body()):
    for todo in todo_list:
        if todo.id == data.id:
            todo.value = data.value
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={
            "message": f"Todo [{data.id}] not found",
            "code": "TODO_NOT_FOUND",
            "status_code": status.HTTP_404_NOT_FOUND
        }
    )


@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={
            "message": f"Todo [{todo_id}] not found",
            "code": "TODO_NOT_FOUND",
            "status_code": status.HTTP_404_NOT_FOUND
        }
    )