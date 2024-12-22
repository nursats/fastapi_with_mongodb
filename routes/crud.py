from fastapi import APIRouter, HTTPException, Depends, Response, status


router = APIRouter(
    prefix="/api/messages",
    tags=['messages']
)

@router.get('/')
def read_messages():
    return 'Hello, world!'