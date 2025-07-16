import httpx
import typing
import typing_extensions

from demo_api_41_py.core import (
    AsyncBaseClient,
    BinaryResponse,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_content,
    to_encodable,
    type_utils,
)
from demo_api_41_py.types import models, params


class PetClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, pet_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> httpx.Response:
        """
        Deletes a pet.

        Delete a pet.

        DELETE /pet/{petId}

        Args:
            petId: Pet id to delete
            request_options: Additional options to customize the HTTP request

        Returns:
            Pet deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.pet.delete(pet_id=123)
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/pet/{pet_id}",
            auth_names=["api_key"],
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    def find_by_status(
        self,
        *,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["available", "pending", "sold"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[typing.List[models.Pet], BinaryResponse]:
        """
        Finds Pets by status.

        Multiple status values can be provided with comma separated strings.

        GET /pet/findByStatus

        Args:
            status: Status values that need to be considered for filter
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.pet.find_by_status()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(
                    item=status,
                    dump_with=typing_extensions.Literal["available", "pending", "sold"],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/pet/findByStatus",
            auth_names=["api_key"],
            query_params=_query,
            cast_to=typing.Union[typing.List[models.Pet], BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, pet_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Union[models.Pet, BinaryResponse]:
        """
        Find pet by ID.

        Returns a single pet.

        GET /pet/{petId}

        Args:
            petId: ID of pet to return
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.pet.get(pet_id=123)
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/pet/{pet_id}",
            auth_names=["api_key"],
            cast_to=typing.Union[models.Pet, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        name: str,
        photo_urls: typing.List[str],
        category: typing.Union[
            typing.Optional[params.Category], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["available", "pending", "sold"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tags: typing.Union[
            typing.Optional[typing.List[params.Tag]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.Pet, BinaryResponse]:
        """
        Add a new pet to the store.

        Add a new pet to the store.

        POST /pet

        Args:
            category: Category
            id: int
            status: pet status in the store
            tags: typing.List[Tag]
            name: str
            photoUrls: typing.List[str]
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.pet.create(name="doggie", photo_urls=["string"], id=10)
        ```
        """
        _json = to_encodable(
            item={
                "category": category,
                "id": id,
                "status": status,
                "tags": tags,
                "name": name,
                "photo_urls": photo_urls,
            },
            dump_with=params._SerializerPet,
        )
        return self._base_client.request(
            method="POST",
            path="/pet",
            auth_names=["api_key"],
            json=_json,
            cast_to=typing.Union[models.Pet, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    def upload_image(
        self,
        *,
        data: httpx._types.FileTypes,
        pet_id: int,
        additional_metadata: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ApiResponse:
        """
        Uploads an image.

        Upload image of the pet.

        POST /pet/{petId}/uploadImage

        Args:
            additionalMetadata: Additional Metadata
            data: httpx._types.FileTypes
            petId: ID of pet to update
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.pet.upload_image(data=open("uploads/file.pdf", "rb"), pet_id=123)
        ```
        """
        _query: QueryParams = {}
        if not isinstance(additional_metadata, type_utils.NotGiven):
            encode_query_param(
                _query,
                "additionalMetadata",
                to_encodable(item=additional_metadata, dump_with=str),
                style="form",
                explode=True,
            )
        _content = to_content(file=data)
        _content_type = "application/octet-stream"
        return self._base_client.request(
            method="POST",
            path=f"/pet/{pet_id}/uploadImage",
            auth_names=["api_key"],
            query_params=_query,
            content=_content,
            content_type=_content_type,
            cast_to=models.ApiResponse,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        name: str,
        photo_urls: typing.List[str],
        category: typing.Union[
            typing.Optional[params.Category], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["available", "pending", "sold"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tags: typing.Union[
            typing.Optional[typing.List[params.Tag]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.Pet, BinaryResponse]:
        """
        Update an existing pet.

        Update an existing pet by Id.

        PUT /pet

        Args:
            category: Category
            id: int
            status: pet status in the store
            tags: typing.List[Tag]
            name: str
            photoUrls: typing.List[str]
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.pet.update(name="doggie", photo_urls=["string"], id=10)
        ```
        """
        _json = to_encodable(
            item={
                "category": category,
                "id": id,
                "status": status,
                "tags": tags,
                "name": name,
                "photo_urls": photo_urls,
            },
            dump_with=params._SerializerPet,
        )
        return self._base_client.request(
            method="PUT",
            path="/pet",
            auth_names=["api_key"],
            json=_json,
            cast_to=typing.Union[models.Pet, BinaryResponse],
            request_options=request_options or default_request_options(),
        )


class AsyncPetClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, pet_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> httpx.Response:
        """
        Deletes a pet.

        Delete a pet.

        DELETE /pet/{petId}

        Args:
            petId: Pet id to delete
            request_options: Additional options to customize the HTTP request

        Returns:
            Pet deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.pet.delete(pet_id=123)
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/pet/{pet_id}",
            auth_names=["api_key"],
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    async def find_by_status(
        self,
        *,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["available", "pending", "sold"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[typing.List[models.Pet], BinaryResponse]:
        """
        Finds Pets by status.

        Multiple status values can be provided with comma separated strings.

        GET /pet/findByStatus

        Args:
            status: Status values that need to be considered for filter
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.pet.find_by_status()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(
                    item=status,
                    dump_with=typing_extensions.Literal["available", "pending", "sold"],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/pet/findByStatus",
            auth_names=["api_key"],
            query_params=_query,
            cast_to=typing.Union[typing.List[models.Pet], BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, pet_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Union[models.Pet, BinaryResponse]:
        """
        Find pet by ID.

        Returns a single pet.

        GET /pet/{petId}

        Args:
            petId: ID of pet to return
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.pet.get(pet_id=123)
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/pet/{pet_id}",
            auth_names=["api_key"],
            cast_to=typing.Union[models.Pet, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        name: str,
        photo_urls: typing.List[str],
        category: typing.Union[
            typing.Optional[params.Category], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["available", "pending", "sold"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tags: typing.Union[
            typing.Optional[typing.List[params.Tag]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.Pet, BinaryResponse]:
        """
        Add a new pet to the store.

        Add a new pet to the store.

        POST /pet

        Args:
            category: Category
            id: int
            status: pet status in the store
            tags: typing.List[Tag]
            name: str
            photoUrls: typing.List[str]
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.pet.create(name="doggie", photo_urls=["string"], id=10)
        ```
        """
        _json = to_encodable(
            item={
                "category": category,
                "id": id,
                "status": status,
                "tags": tags,
                "name": name,
                "photo_urls": photo_urls,
            },
            dump_with=params._SerializerPet,
        )
        return await self._base_client.request(
            method="POST",
            path="/pet",
            auth_names=["api_key"],
            json=_json,
            cast_to=typing.Union[models.Pet, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    async def upload_image(
        self,
        *,
        data: httpx._types.FileTypes,
        pet_id: int,
        additional_metadata: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ApiResponse:
        """
        Uploads an image.

        Upload image of the pet.

        POST /pet/{petId}/uploadImage

        Args:
            additionalMetadata: Additional Metadata
            data: httpx._types.FileTypes
            petId: ID of pet to update
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.pet.upload_image(data=open("uploads/file.pdf", "rb"), pet_id=123)
        ```
        """
        _query: QueryParams = {}
        if not isinstance(additional_metadata, type_utils.NotGiven):
            encode_query_param(
                _query,
                "additionalMetadata",
                to_encodable(item=additional_metadata, dump_with=str),
                style="form",
                explode=True,
            )
        _content = to_content(file=data)
        _content_type = "application/octet-stream"
        return await self._base_client.request(
            method="POST",
            path=f"/pet/{pet_id}/uploadImage",
            auth_names=["api_key"],
            query_params=_query,
            content=_content,
            content_type=_content_type,
            cast_to=models.ApiResponse,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        name: str,
        photo_urls: typing.List[str],
        category: typing.Union[
            typing.Optional[params.Category], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["available", "pending", "sold"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tags: typing.Union[
            typing.Optional[typing.List[params.Tag]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.Pet, BinaryResponse]:
        """
        Update an existing pet.

        Update an existing pet by Id.

        PUT /pet

        Args:
            category: Category
            id: int
            status: pet status in the store
            tags: typing.List[Tag]
            name: str
            photoUrls: typing.List[str]
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.pet.update(name="doggie", photo_urls=["string"], id=10)
        ```
        """
        _json = to_encodable(
            item={
                "category": category,
                "id": id,
                "status": status,
                "tags": tags,
                "name": name,
                "photo_urls": photo_urls,
            },
            dump_with=params._SerializerPet,
        )
        return await self._base_client.request(
            method="PUT",
            path="/pet",
            auth_names=["api_key"],
            json=_json,
            cast_to=typing.Union[models.Pet, BinaryResponse],
            request_options=request_options or default_request_options(),
        )
