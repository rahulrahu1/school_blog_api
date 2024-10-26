from fastapi import FastAPI
from app.routes import router as posts_router
from app.database import get_db

app = FastAPI()

app.include_router(posts_router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the School Blog API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)