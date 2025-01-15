import asyncio

from google.protobuf.json_format import MessageToDict

from tests.client.test_client import grpc_client
from tests.client.test_request import request


def test_GRPCAsyncServerUpdateBets():
    result = asyncio.get_event_loop().run_until_complete(grpc_client.update_bets(request))
    assert isinstance(result, object)
    print(f"Result: {MessageToDict(result)}")
