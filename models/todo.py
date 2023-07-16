from sqlalchemy import Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base

from connection import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)