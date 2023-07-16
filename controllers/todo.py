from fastapi import APIRouter, HTTPException, status
from typing import List

from fastapi.params import Depends
from sqlalchemy.orm import Session

from dto.todo import TodoResponse, TodoCreate, TodoUpdate
from models.todo import Todo
from connection import get_db

todo_router = APIRouter()

# Create a new Todo
@todo_router.post("/todos", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = Todo(title=todo.title, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


# Get all Todos
@todo_router.get("/todos", response_model=List[TodoResponse])
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return todos


# Update a specific Todo by ID
@todo_router.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    existing_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not existing_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    existing_todo.title = todo.title
    existing_todo.description = todo.description
    db.commit()
    db.refresh(existing_todo)
    return existing_todo


# Delete a specific Todo by ID
@todo_router.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    existing_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not existing_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(existing_todo)
    db.commit()
