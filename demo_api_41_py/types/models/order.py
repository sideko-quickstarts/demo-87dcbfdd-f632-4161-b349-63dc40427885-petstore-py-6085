import pydantic
import typing
import typing_extensions


class Order(pydantic.BaseModel):
    """
    Order
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
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
    """
    Order Status
    """
