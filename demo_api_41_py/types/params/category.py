import pydantic
import typing
import typing_extensions


class Category(typing_extensions.TypedDict):
    """
    Category
    """

    id: typing_extensions.NotRequired[int]

    name: typing_extensions.NotRequired[str]


class _SerializerCategory(pydantic.BaseModel):
    """
    Serializer for Category handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
