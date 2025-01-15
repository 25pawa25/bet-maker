from typing import List

from sqlalchemy import and_, select, update

from db.postgres.models.bet import Bet, BetStatus
from repository.interfaces.entity.abc_bet_repository import AbstractBetRepository
from repository.postgres_implementation.base_repository import SQLRepository
from schemas.entities.bet_entity import BetEntity


class SQLBetRepository(SQLRepository, AbstractBetRepository):
    class_model = Bet
    entity_class = BetEntity

    async def create_bet(self, **fields) -> BetEntity:
        """
        Creating a bet
        Args:
            **fields: fields of bet
        Returns:
            EventEntity
        """
        return await self.add(self.entity_class(**fields))

    async def update_bets(self, event_id: str, **fields):
        """
        Updating a bets by event_id
        Args:
            event_id: bet id
            **fields: fields of bet
        Returns:
            EventEntity
        """
        stmt = (
            update(self.class_model)
            .where(
                and_(
                    self.class_model.event_id == event_id,
                    self.class_model.status == BetStatus.PENDING,
                )
            )
            .values(**fields)
        )

        await self.session.execute(stmt)
        await self.session.commit()

    async def get_bets_by(
        self, page: int = 1, page_size: int = 10, **fields
    ) -> List[BetEntity]:
        """
        Get bets by fields
        Args:
            page: number of the page
            page_size: size of the page
            **fields: fields to filter
        Returns:
            EventEntity
        """
        filters = []
        if deadline := fields.pop("deadline", None):
            filters.append(self.class_model.deadline > deadline)
        stmt = (
            select(self.class_model)
            .where(and_(*filters))
            .filter_by(**fields)
            .limit(page_size)
            .offset((page - 1) * page_size)
        )
        result = await self.session.execute(stmt)
        return [self.to_entity(instance) for instance in result.scalars().all()]
