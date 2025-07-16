from demo_api_41_py.core import AsyncBaseClient, SyncBaseClient
from demo_api_41_py.resources.store.order import AsyncOrderClient, OrderClient


class StoreClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.order = OrderClient(base_client=self._base_client)


class AsyncStoreClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.order = AsyncOrderClient(base_client=self._base_client)
