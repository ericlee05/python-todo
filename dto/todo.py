from pydantic import BaseModel


class TodoResponse(BaseModel):
    id: int
    title: str
    description: str


class TodoCreate(BaseModel):
    title: str
    description: str


class TodoUpdate(BaseModel):
    title: str
    description: str
