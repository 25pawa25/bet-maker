from datetime import datetime
from typing import List

from common.exceptions.event import EventNotExists
from db.postgres.connection import get_postgres_session
from db.postgres.models.bet import BetStatus
from repository.grpc_implementation.event_repository import get_grpc_event_repository
from repository.interfaces.entity.abc_bet_repository import AbstractBetRepository
from repository.interfaces.grpc.abc_event_repository import AbstractEventRepository
from repository.postgres_implementation.bet_repository import SQLBetRepository
from schemas.request.bet import BetSchema, UpdateBetSchema
from schemas.response.bet import BetResponse
from services.bet.abc_bet import AbstractBetService


class BetService(AbstractBetService):
    def __init__(
        self,
        event_repository: AbstractEventRepository,
        bet_repository: AbstractBetRepository,
    ) -> None:
        self.event_repository = event_repository
        self.bet_repository = bet_repository

    async def create_bet(self, schema: BetSchema) -> BetResponse:
        """
        Create bet
        Args:
            schema: BetSchema
        Returns:
            BetResponse
        """
        if not await self.event_repository.check_if_event_exists(
            event_id=str(schema.event_id)
        ):
            raise EventNotExists("Event does not exist", event_id=schema.event_id)
        event = await self.bet_repository.create_bet(**schema.dict())
        return BetResponse.from_orm(event)

    async def update_bets(self, schema: UpdateBetSchema):
        """
        Update bet
        Args:
            schema: UpdateBetSchema
        Returns:
            List of BetResponse
        """
        # Проверка статуса у события и обновление ставки в зависимости от него
        await self.bet_repository.update_bets(
            event_id=schema.event_id,
            status=BetStatus.WIN if schema.status == "first_win" else BetStatus.FAILED,
            updated_at=datetime.utcnow(),
        )

    async def get_bets(self) -> List[BetResponse]:
        """
        Get bet by user_id
        Returns:
            List of BetResponse
        """
        bets_db = await self.bet_repository.get_bets_by()
        return [BetResponse.from_orm(bet) for bet in bets_db]

    async def get_available_events(self, **kwargs) -> List[BetResponse]:
        """
        Get available events
        Returns:
            List of the available events
        """
        return await self.event_repository.get_available_events()


async def get_bet_service():
    session = await get_postgres_session()
    return BetService(
        bet_repository=SQLBetRepository(session=session),
        event_repository=get_grpc_event_repository(),
    )
