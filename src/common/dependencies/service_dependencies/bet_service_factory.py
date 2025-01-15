from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from common.dependencies.registrator import add_factory_to_mapper
from db.postgres.connection import get_async_session
from repository.grpc_implementation.event_repository import get_grpc_event_repository
from repository.postgres_implementation.bet_repository import SQLBetRepository
from services import BetService
from services.bet.abc_bet import AbstractBetService


@add_factory_to_mapper(AbstractBetService)
def create_bet_service(
    session: AsyncSession = Depends(get_async_session),
):
    return BetService(
        bet_repository=SQLBetRepository(session=session),
        event_repository=get_grpc_event_repository(),
    )
