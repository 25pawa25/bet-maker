from typing import List

from fastapi import APIRouter, Depends, status
from loguru import logger

from schemas.request.bet import BetSchema
from schemas.response.bet import BetResponse
from services.bet.abc_bet import AbstractBetService

bet_router = APIRouter(prefix="/bet", tags=["Actions with single bet"])
bets_router = APIRouter(prefix="/bets", tags=["Actions with bets"])


@bet_router.post(
    "",
    summary="Create bet",
    description="Create bet",
    response_model=BetResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_bet(
    request: BetSchema,
    bet_service: AbstractBetService = Depends(),
) -> BetResponse:
    """
    Create a bet
    Args:
        request: BetSchema
        bet_service: BetService
    Returns:
        BetResponse
    """
    logger.info(f"Create bet")
    return await bet_service.create_bet(request)


@bets_router.get("", summary="Get bets", description="Get bets")
async def get_bets(
    bet_service: AbstractBetService = Depends(),
) -> List[BetResponse]:
    """
    Get bet by id
    Args:
        bet_service: BetService
    Returns:
        List of BetResponse
    """
    logger.info(f"Get bets")
    return await bet_service.get_bets()
