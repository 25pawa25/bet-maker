from fastapi import APIRouter

from clients.api.v1.bet import bet_router, bets_router
from clients.api.v1.event import event_router

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(event_router)
v1_router.include_router(bet_router)
v1_router.include_router(bets_router)
