import uuid
from datetime import datetime

from pydantic import BaseModel

from db.postgres.models.bet import BetStatus


class BetResponse(BaseModel):
    id: uuid.UUID
    event_id: uuid.UUID
    amount: float
    status: BetStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
