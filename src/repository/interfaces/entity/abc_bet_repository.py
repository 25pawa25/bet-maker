from abc import abstractmethod
from typing import List

from repository.base.abc_entity_repository import BaseRepository
from schemas.entities.base_entity import BaseEntity


class AbstractBetRepository(BaseRepository):
    @abstractmethod
    async def create_bet(self, **fields) -> BaseEntity:
        pass

    @abstractmethod
    async def update_bets(self, event_id: str, **fields):
        pass

    @abstractmethod
    async def get_bets_by(
        self, page: int = 1, page_size: int = 10, **fields
    ) -> List[BaseEntity]:
        pass
