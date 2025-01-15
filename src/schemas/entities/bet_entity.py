import uuid
from datetime import datetime

from pydantic import Field

from db.postgres.models.bet import BetStatus
from schemas.entities.base_entity import BaseEntity


class BetEntity(BaseEntity):
    event_id: uuid.UUID
    amount: float
    status: BetStatus = BetStatus.PENDING
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True
