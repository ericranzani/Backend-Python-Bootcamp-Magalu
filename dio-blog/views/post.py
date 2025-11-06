from datetime import datetime
from pydantic import BaseModel

class PostOut(BaseModel):
    title: str
    published_at: datetime
    author: str 