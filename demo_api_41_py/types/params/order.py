import pydantic
import typing
import typing_extensions


class Order(typing_extensions.TypedDict):
    """
    Order
    """

    complete: typing_extensions.NotRequired[bool]

    id: typing_extensions.NotRequired[int]

    pet_id: typing_extensions.NotRequired[int]

    quantity: typing_extensions.NotRequired[int]

    ship_date: typing_extensions.NotRequired[str]

    status: typing_extensions.NotRequired[
        typing_extensions.Literal["approved", "delivered", "placed"]
    ]
    """
    Order Status
    """


class _SerializerOrder(pydantic.BaseModel):
    """
    Serializer for Order handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    complete: typing.Optional[bool] = pydantic.Field(alias="complete", default=None)
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    pet_id: typing.Optional[int] = pydantic.Field(alias="petId", default=None)
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    ship_date: typing.Optional[str] = pydantic.Field(alias="shipDate", default=None)
    status: typing.Optional[
        typing_extensions.Literal["approved", "delivered", "placed"]
    ] = pydantic.Field(alias="status", default=None)
