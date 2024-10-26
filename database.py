from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Depends
from app.config import DATABASE_URI

client = AsyncIOMotorClient(DATABASE_URI)
database = client.school_blog_db

async def get_db():
    db = client.school_blog_db
    return db
