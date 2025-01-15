from grpc.aio import insecure_channel

from clients.grpc.proto.bet.bet_pb2_grpc import BetStub
from clients.grpc.proto.line_provider.line_provider_pb2_grpc import LineProviderStub
from core.config import settings


class GRPCClient:
    def __init__(self):
        self.channel = insecure_channel(f"{settings.grpc_server.host}:{settings.grpc_server.port}")
        self.stub = BetStub(self.channel)
        self.auth_token = f"Bearer {settings.grpc_server.auth_token}"
        self.metadata = [("authorization", self.auth_token)]

    async def update_bets(self, request):
        return await self.stub.UpdateBets(request, metadata=self.metadata)


grpc_client = GRPCClient()
