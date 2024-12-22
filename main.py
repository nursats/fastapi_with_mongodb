from fastapi import FastAPI
import certifi
import os
from dotenv import load_dotenv

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from .routes import crud

app = FastAPI()

load_dotenv()

mongodb_url = os.getenv("MONGODB_URL")

client = MongoClient(mongodb_url, server_api=ServerApi('1'), tlsCAFile=certifi.where())


app.include_router(crud.router)

