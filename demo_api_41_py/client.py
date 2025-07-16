import httpx
import typing

from demo_api_41_py.core import AsyncBaseClient, AuthKey, SyncBaseClient
from demo_api_41_py.environment import Environment, _get_base_url
from demo_api_41_py.resources.pet import AsyncPetClient, PetClient
from demo_api_41_py.resources.store import AsyncStoreClient, StoreClient


class Client:
    def __init__(
        self,
        *,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
        base_url: typing.Optional[str] = None,
        environment: Environment = Environment.ENVIRONMENT,
        api_key: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = SyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.Client(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth(
            "api_key", AuthKey(name="api_key", location="header", val=api_key)
        )
        self.pet = PetClient(base_client=self._base_client)
        self.store = StoreClient(base_client=self._base_client)


class AsyncClient:
    def __init__(
        self,
        *,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        base_url: typing.Optional[str] = None,
        environment: Environment = Environment.ENVIRONMENT,
        api_key: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = AsyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.AsyncClient(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth(
            "api_key", AuthKey(name="api_key", location="header", val=api_key)
        )
        self.pet = AsyncPetClient(base_client=self._base_client)
        self.store = AsyncStoreClient(base_client=self._base_client)
