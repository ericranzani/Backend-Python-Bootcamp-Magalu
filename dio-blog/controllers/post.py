from datetime import datetime, timezone
from typing import Annotated
from fastapi import Cookie, Response, status, Header, APIRouter
from schemas.post import PostIn
from views.post import PostOut

router = APIRouter(prefix='/posts')

fake_db = [
    {'title': f'Criando uma aplicação com Django', 'date': datetime.now(timezone.utc), "published": True}, 
    {'title': f'Internacionalizando uma app FastAPI', 'date': datetime.now(timezone.utc), "published": True},
    {'title': f'Criando uma aplicação com Flask', 'date': datetime.now(timezone.utc), "published": True}, 
    {'title': f'Internacionalizando uma app Starlett', 'date': datetime.now(timezone.utc), "published": False},
]

# request body
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_post(post: PostIn):
    fake_db.append(post.model_dump())
    return post

# query parameters
@router.get('/', response_model=list[PostOut])
def read_posts(
    response: Response, 
    published: bool, 
    limit: int, 
    skip: int = 0, 
    ads_is: Annotated[str | None, Cookie()] = None,
    user_agent: Annotated[str | None, Header()] = None, 
):
    response.set_cookie(key='user', value='test_cookie')
    print(f'Cookie: {ads_is}')
    print(f'User-Agent: {user_agent}')
    # return fake_db[skip: skip + limit] # simpler version - precisa tirar o valor boolean
    tail = skip + limit
    return [post for post in fake_db[skip: tail] if post['published'] is published]

# path parameters
@router.get('/{framework}', response_model=PostOut)
def read_framework_posts(framework: str):
    return {
        "posts": [
            {'title': f'Criando uma aplicação com {framework}', 'date': datetime.now(timezone.utc)}, 
            {'title': f'Internacionalizando uma app {framework}', 'date': datetime.now(timezone.utc)},
        ]
    }