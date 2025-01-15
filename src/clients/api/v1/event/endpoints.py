from typing import List

from fastapi import APIRouter, Depends, status
from loguru import logger

from schemas.response.event import EventResponse
from services.bet.abc_bet import AbstractBetService

router = APIRouter(prefix="/events", tags=["Events actions"])


@router.get(
    "",
    summary="Get events",
    description="Get all available events",
    status_code=status.HTTP_200_OK,
)
async def get_events(
    bet_service: AbstractBetService = Depends(),
) -> List[EventResponse]:
    """
    Get available events
    Args:
        bet_service: BetService
    Returns:
        EventResponse
    """
    logger.info(f"Get all available events")
    return await bet_service.get_available_events()
