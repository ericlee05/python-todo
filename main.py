import uvicorn
from fastapi import FastAPI
from sqlalchemy.orm import declarative_base

from connection import create_tables
from controllers.todo import todo_router

app = FastAPI()

app.include_router(todo_router)

create_tables()

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)