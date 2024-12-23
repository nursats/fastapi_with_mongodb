from typing import Optional
from pydantic import BaseModel, Field


class Message(BaseModel):
    content: str
    from_user_id: int
    to_user_id: int

class MessageInDB(Message):
    id: str = Field(default_factory=str)
    publish_timestamp: float
    edit_timestamp: Optional[float] = None