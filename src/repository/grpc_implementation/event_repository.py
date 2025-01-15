from functools import lru_cache

from google.protobuf.json_format import MessageToDict
from grpc.aio import AioRpcError, insecure_channel
from typing_extensions import List

from clients.grpc.proto.line_provider import line_provider_pb2
from clients.grpc.proto.line_provider.line_provider_pb2_grpc import LineProviderStub
from common.exceptions.grpc import GRPCConnectionException
from core.config import settings
from repository.interfaces.grpc.abc_event_repository import AbstractEventRepository
from schemas.response.event import EventResponse


class GRPCEventRepository(AbstractEventRepository):
    def __init__(self):
        self.metadata = settings.line_provider_grpc.metadata

    @property
    def channel(self):
        return insecure_channel(settings.line_provider_grpc.url)

    @property
    def stub(self):
        return LineProviderStub(self.channel)

    async def get_available_events(self) -> List[EventResponse]:
        """
        Get available events
        Returns:
            List[EventResponse]
        """
        try:
            response = await self.stub.GetEvents(line_provider_pb2.GetEventsRequest())
            events = MessageToDict(response, preserving_proto_field_name=True)
            return [EventResponse(**event) for event in events.get("events", [])]
        except AioRpcError:
            raise GRPCConnectionException("Error while getting available events")

    async def check_if_event_exists(self, event_id: str) -> bool:
        """
        Check if event exists
        Returns:
            bool
        """
        try:
            response = await self.stub.CheckIfEventExists(
                line_provider_pb2.CheckIfEventExistsRequest(event_id=event_id)
            )
            event = MessageToDict(response, preserving_proto_field_name=True)
            return event.get("id") is not None
        except AioRpcError:
            raise GRPCConnectionException("Error while checking event")


@lru_cache()
def get_grpc_event_repository() -> AbstractEventRepository:
    return GRPCEventRepository()
