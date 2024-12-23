from fastapi import FastAPI
from routes import crud
from db.database import collection
from contextlib import asynccontextmanager


app = FastAPI()

@asynccontextmanager
async def startup_db():
    print("Connecting to the database...")
    assert collection is not None, "Failed to connect to the database"

app.include_router(crud.router)


@app.get("/")
def root():
    return {
        "message": "welcome to my project",
        "description": "This is a demo project",
        "contact": "nursat.seitov12@gmail.com"
        }
