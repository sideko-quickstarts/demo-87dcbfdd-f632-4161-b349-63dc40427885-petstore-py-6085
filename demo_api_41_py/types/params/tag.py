import pydantic
import typing
import typing_extensions


class Tag(typing_extensions.TypedDict):
    """
    Tag
    """

    id: typing_extensions.NotRequired[int]

    name: typing_extensions.NotRequired[str]


class _SerializerTag(pydantic.BaseModel):
    """
    Serializer for Tag handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
