import httpx
import typing
import typing_extensions

from demo_api_41_py.core import (
    AsyncBaseClient,
    BinaryResponse,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_form_urlencoded,
    type_utils,
)
from demo_api_41_py.types import models, params


class OrderClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, order_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> httpx.Response:
        """
        Delete purchase order by identifier.

        For valid response try integer IDs with value < 1000. Anything above 1000 or non-integers will generate API errors.

        DELETE /store/order/{orderId}

        Args:
            orderId: ID of the order that needs to be deleted
            request_options: Additional options to customize the HTTP request

        Returns:
            order deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.store.order.delete(order_id=123)
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/store/order/{order_id}",
            auth_names=["api_key"],
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, order_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Union[models.Order, BinaryResponse]:
        """
        Find purchase order by ID.

        For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

        GET /store/order/{orderId}

        Args:
            orderId: ID of order that needs to be fetched
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.store.order.get(order_id=123)
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/store/order/{order_id}",
            auth_names=["api_key"],
            cast_to=typing.Union[models.Order, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        complete: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pet_id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        quantity: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ship_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal["approved", "delivered", "placed"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Order:
        """
        Place an order for a pet.

        Place a new order in the store.

        POST /store/order

        Args:
            complete: bool
            id: int
            petId: int
            quantity: int
            shipDate: str
            status: Order Status
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.store.order.create(id=10, pet_id=198772, quantity=7, status="approved")
        ```
        """
        _data = to_form_urlencoded(
            item={
                "complete": complete,
                "id": id,
                "pet_id": pet_id,
                "quantity": quantity,
                "ship_date": ship_date,
                "status": status,
            },
            dump_with=params._SerializerOrder,
            style={
                "complete": "form",
                "id": "form",
                "petId": "form",
                "quantity": "form",
                "shipDate": "form",
                "status": "form",
            },
            explode={
                "complete": True,
                "id": True,
                "petId": True,
                "quantity": True,
                "shipDate": True,
                "status": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/store/order",
            auth_names=["api_key"],
            data=_data,
            cast_to=models.Order,
            request_options=request_options or default_request_options(),
        )


class AsyncOrderClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, order_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> httpx.Response:
        """
        Delete purchase order by identifier.

        For valid response try integer IDs with value < 1000. Anything above 1000 or non-integers will generate API errors.

        DELETE /store/order/{orderId}

        Args:
            orderId: ID of the order that needs to be deleted
            request_options: Additional options to customize the HTTP request

        Returns:
            order deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.store.order.delete(order_id=123)
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/store/order/{order_id}",
            auth_names=["api_key"],
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, order_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Union[models.Order, BinaryResponse]:
        """
        Find purchase order by ID.

        For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

        GET /store/order/{orderId}

        Args:
            orderId: ID of order that needs to be fetched
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.store.order.get(order_id=123)
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/store/order/{order_id}",
            auth_names=["api_key"],
            cast_to=typing.Union[models.Order, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        complete: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pet_id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        quantity: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ship_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal["approved", "delivered", "placed"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Order:
        """
        Place an order for a pet.

        Place a new order in the store.

        POST /store/order

        Args:
            complete: bool
            id: int
            petId: int
            quantity: int
            shipDate: str
            status: Order Status
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.store.order.create(
            id=10, pet_id=198772, quantity=7, status="approved"
        )
        ```
        """
        _data = to_form_urlencoded(
            item={
                "complete": complete,
                "id": id,
                "pet_id": pet_id,
                "quantity": quantity,
                "ship_date": ship_date,
                "status": status,
            },
            dump_with=params._SerializerOrder,
            style={
                "complete": "form",
                "id": "form",
                "petId": "form",
                "quantity": "form",
                "shipDate": "form",
                "status": "form",
            },
            explode={
                "complete": True,
                "id": True,
                "petId": True,
                "quantity": True,
                "shipDate": True,
                "status": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/store/order",
            auth_names=["api_key"],
            data=_data,
            cast_to=models.Order,
            request_options=request_options or default_request_options(),
        )
