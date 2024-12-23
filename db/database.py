import certifi
import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi


load_dotenv()

mongodb_url = os.getenv("MONGODB_URL")

client =  AsyncIOMotorClient(mongodb_url, server_api=ServerApi('1'), tlsCAFile=certifi.where())

db = client.messages_db
collection = db.messages