from fastapi import status, APIRouter
from schemas.post import PostIn, PostUpdateIn
from views.post import PostOut
from services.post import PostService
from models.post import posts
from database import database

router = APIRouter(prefix='/posts')

services = PostService()

# query parameters
@router.get("/", response_model=list[PostOut])
async def read_posts(published: bool, limit: int, skip: int = 0):
    return await services.read_all(published=published, limit=limit, skip=skip)
    
# request body
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
async def create_post(post: PostIn):
    return {**post.model_dump(), "id": await services.create(post)}

# buscando por id
@router.get("/{id}", response_model=PostOut)
async def read_post(id: int):
    return await services.read(id)

@router.patch("/{id}", response_model=PostOut)
async def update_post(id: int, post: PostUpdateIn):
    return await services.update(id = id, post = post)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_post(id: int):
    await services.delete(id)