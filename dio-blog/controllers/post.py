from datetime import datetime, timezone
from typing import Annotated
from fastapi import Cookie, Response, status, Header, APIRouter
from schemas.post import PostIn
from views.post import PostOut

router = APIRouter(prefix='/posts')

# request body
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_post(post: PostIn):
    # fake_db.append(post.model_dump())
    return post

# query parameters
@router.get('/', response_model=list[PostOut])
def read_posts(
    response: Response, 
    published: bool, 
    limit: int, 
    skip: int = 0
):
    tail = skip + limit

# path parameters
@router.get('/{framework}', response_model=PostOut)
def read_framework_posts(framework: str):
    return {
        "posts": [
            {'title': f'Criando uma aplicação com {framework}', 'date': datetime.now(timezone.utc)}, 
            {'title': f'Internacionalizando uma app {framework}', 'date': datetime.now(timezone.utc)},
        ]
    }