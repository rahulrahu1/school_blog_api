from fastapi import APIRouter, Depends
from app.database import get_db
from app.models import Post, CreatePost
from pydantic import ValidationError

router = APIRouter()

@router.post("/posts/", response_model=Post)
async def create_post(post: CreatePost, db: AsyncIOMotorClient = Depends(get_db)):
    result = db.posts.insert_one(post.dict())
    return Post(**post.dict(), id=result.inserted_id)

@router.get("/posts/", response_model=list)
async def get_posts(db: AsyncIOMotorClient = Depends(get_db)):
    return list(db.posts.find({}))

@router.get("/posts/{post_id}", response_model=Post)
async def get_post(post_id: str, db: AsyncIOMotorClient = Depends(get_db)):
    return db.posts.find_one({"_id": post_id})

@router.put("/posts/{post_id}", response_model=Post)
async def update_post(post_id: str, post: CreatePost, db: AsyncIOMotorClient = Depends(get_db)):
    result = db.posts.update_one({"_id": post_id}, {"$set": post.dict()})
    return db.posts.find_one({"_id": post_id})

@router.delete("/posts/{post_id}")
async def delete_post(post_id: str, db: AsyncIOMotorClient = Depends(get_db)):
    result = db.posts.delete_one({"_id": post_id})
    return {"message": "Post deleted successfully"}
