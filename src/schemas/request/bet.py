import uuid

from pydantic import BaseModel, Field


class BetSchema(BaseModel):
    event_id: uuid.UUID
    amount: float = Field(example=1234.56, gt=0)


class UpdateBetSchema(BaseModel):
    event_id: str
    status: str
