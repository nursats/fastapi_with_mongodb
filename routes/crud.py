from datetime import datetime
from typing import List
from bson import ObjectId
from fastapi import APIRouter, HTTPException, Depends, Response, status
from fastapi.responses import JSONResponse
from schemas import schemas
from db.database import collection
from motor.motor_asyncio import AsyncIOMotorClient

router = APIRouter(
    prefix="/api",
    tags=['messages']
)

@router.post('/messages', status_code=status.HTTP_201_CREATED, response_model=schemas.MessageInDB)
async def create_message(message: schemas.Message):
    message_dict = message.model_dump()
    message_dict['publish_timestamp'] = datetime.now().timestamp()
    result = await collection.insert_one(message_dict)
    message_dict['id'] = str(result.inserted_id)
    return message_dict

@router.get('/messages/{id}', response_model=schemas.MessageInDB)
async def read_message(id: str):
    message = await collection.find_one({"_id": ObjectId(id)})
    if message:
        message['id'] = str(message['_id'])
        return message
    raise HTTPException(status_code=404, detail="Message not found")  


@router.get("/messages/", response_model=List[schemas.MessageInDB])
async def read_messages(from_user_id: int, to_user_id: int):
    messages = await collection.find({"from_user_id": from_user_id, "to_user_id": to_user_id}).to_list(1000)
    for message in messages:
        message['id'] = str(message['_id'])
    return sorted(messages, key=lambda x: x['publish_timestamp'], reverse=True)


@router.put('/messages/{id}', response_model=schemas.MessageInDB)
async def update_message(id: str, message: schemas.Message):
    message_dict = message.model_dump()
    message_dict['edit_timestamp'] = datetime.now().timestamp()
    result = await collection.update_one({"_id": ObjectId(id)}, {"$set": message_dict})
    if result.modified_count == 1:
        message = await collection.find_one({"_id": ObjectId(id)})
        message['id'] = str(message['_id'])
        return message
    raise HTTPException(status_code=404, detail="Message not found")


@router.delete('/messages/{id}', response_class=Response, status_code=status.HTTP_204_NO_CONTENT)
async def delete_message(id: str):
    result = await collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return JSONResponse(content={"id": id})
    raise HTTPException(status_code=404, detail="Message not found")

@router.get('/')
def read_messages():
    return 'Hello, world!'