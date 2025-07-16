import httpx
import pydantic
import pytest

from demo_api_41_py import AsyncClient, Client
from demo_api_41_py.core import BinaryResponse
from demo_api_41_py.environment import Environment
from demo_api_41_py.types import models


def test_create_200_success_all_params():
    """Tests a POST request to the /store/order endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Order

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.store.order.create(
        complete=True,
        id=10,
        pet_id=198772,
        quantity=7,
        ship_date="1970-01-01T00:00:00",
        status="approved",
    )
    try:
        pydantic.TypeAdapter(models.Order).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params():
    """Tests a POST request to the /store/order endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Order

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.store.order.create(
        complete=True,
        id=10,
        pet_id=198772,
        quantity=7,
        ship_date="1970-01-01T00:00:00",
        status="approved",
    )
    try:
        pydantic.TypeAdapter(models.Order).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_all_params():
    """Tests a GET request to the /store/order/{orderId} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[models.Order, BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.store.order.get(order_id=123)
    try:
        pydantic.TypeAdapter(models.Order).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params():
    """Tests a GET request to the /store/order/{orderId} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[models.Order, BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.store.order.get(order_id=123)
    try:
        pydantic.TypeAdapter(models.Order).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"


def test_delete_200_success_all_params():
    """Tests a DELETE request to the /store/order/{orderId} endpoint.

    Operation: delete
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : httpx.Response

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = client.store.order.delete(order_id=123)
    assert isinstance(response, httpx.Response)


@pytest.mark.asyncio
async def test_await_delete_200_success_all_params():
    """Tests a DELETE request to the /store/order/{orderId} endpoint.

    Operation: delete
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : httpx.Response

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_key="API_KEY", environment=Environment.MOCK_SERVER)
    response = await client.store.order.delete(order_id=123)
    assert isinstance(response, httpx.Response)
