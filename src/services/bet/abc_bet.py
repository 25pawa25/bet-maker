from abc import ABC, abstractmethod
from typing import List

from schemas.request.bet import BetSchema, UpdateBetSchema
from schemas.response.bet import BetResponse
from schemas.response.event import EventResponse


class AbstractBetService(ABC):
    @abstractmethod
    async def create_bet(self, schema: BetSchema) -> BetResponse:
        ...

    @abstractmethod
    async def update_bets(self, schema: UpdateBetSchema):
        ...

    @abstractmethod
    async def get_bets(self) -> List[BetResponse]:
        ...

    @abstractmethod
    async def get_available_events(self, **kwargs) -> List[EventResponse]:
        ...
