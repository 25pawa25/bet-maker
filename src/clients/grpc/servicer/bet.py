import uuid
from functools import lru_cache
from typing import Optional

import grpc
from loguru import logger

from clients.grpc.proto.bet import bet_pb2
from clients.grpc.proto.bet.bet_pb2_grpc import BetServicer
from common.exceptions import IntegrityDataError
from schemas.request.bet import UpdateBetSchema
from services.bet.abc_bet import AbstractBetService
from services.bet.bet import get_bet_service


class BetServicer(BetServicer):
    def __init__(self):
        self.bet_service: Optional[AbstractBetService] = None

    async def init_services(self):
        self.bet_service = await get_bet_service()

    async def UpdateBets(self, request, context) -> bet_pb2.UpdateBetsResponse:
        """
        GRPC update bets
        Args:
            request: GRPC request object
            context: GRPC context object for response
        Returns:
            CreateUserBalanceResponse
            context INTERNAL if error in service working
        """
        try:
            if not (event_id := request.event_id) or not (status := request.status):
                raise IntegrityDataError("Bad request")
            uuid.UUID(event_id)
            await self.bet_service.update_bets(
                schema=UpdateBetSchema(event_id=event_id, status=status)
            )
            return bet_pb2.UpdateBetsResponse()
        except Exception as e:
            error_msg = "Error occurred: " + str(e)
            context.set_details(error_msg)
            logger.opt(exception=e).error(error_msg)
            context.set_code(grpc.StatusCode.INTERNAL)


@lru_cache
async def get_bet_servicer():
    servicer = BetServicer()
    await servicer.init_services()
    return servicer
