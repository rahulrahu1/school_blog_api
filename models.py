from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
    title: str
    content: str
    author: str
    published_date: Optional[str] = None

class CreatePost(BaseModel):
    title: str
    content: str
    author: str
