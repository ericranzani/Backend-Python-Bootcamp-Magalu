from datetime import datetime, timezone
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

fake_db = [
    {'title': f'Criando uma aplicação com Django', 'date': datetime.now(timezone.utc), "published": True}, 
    {'title': f'Internacionalizando uma app FastAPI', 'date': datetime.now(timezone.utc), "published": True},
    {'title': f'Criando uma aplicação com Flask', 'date': datetime.now(timezone.utc), "published": True}, 
    {'title': f'Internacionalizando uma app Starlett', 'date': datetime.now(timezone.utc), "published": False},
]

class Post(BaseModel):
    title: str
    date: datetime = datetime.now(timezone.utc)
    published: bool = False
    author: str | None = None

# request body
@app.post('/posts/', status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    fake_db.append(post.model_dump())
    return post

# query parameters
@app.get('/posts/')
def read_posts(published: bool, limit: int, skip: int = 0):
    # return fake_db[skip: skip + limit] # simpler version - precisa tirar o valor boolean
    return [post for post in fake_db[skip: skip + limit] if post['published'] is published]


# path parameters
@app.get('/posts/{framework}')
def read_framework_posts(framework: str):
    return {
        "posts": [
            {'title': f'Criando uma aplicação com {framework}', 'date': datetime.now(timezone.utc)}, 
            {'title': f'Internacionalizando uma app {framework}', 'date': datetime.now(timezone.utc)},
        ]
    }
