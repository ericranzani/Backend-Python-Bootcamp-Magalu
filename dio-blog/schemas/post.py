from datetime import datetime, timezone
from pydantic import BaseModel


class PostIn(BaseModel):
    title: str
    date: datetime = datetime.now(timezone.utc)
    published: bool = False
    author: str | None = None