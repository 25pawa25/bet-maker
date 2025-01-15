import uuid
from datetime import datetime

from pydantic import BaseModel


class EventResponse(BaseModel):
    id: uuid.UUID
    coefficient: float
    status: str
    deadline: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
