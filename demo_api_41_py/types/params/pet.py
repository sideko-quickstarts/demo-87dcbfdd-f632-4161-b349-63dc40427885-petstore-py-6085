import pydantic
import typing
import typing_extensions

from .category import Category, _SerializerCategory
from .tag import Tag, _SerializerTag


class Pet(typing_extensions.TypedDict):
    """
    Pet
    """

    category: typing_extensions.NotRequired[Category]

    id: typing_extensions.NotRequired[int]

    name: typing_extensions.Required[str]

    photo_urls: typing_extensions.Required[typing.List[str]]

    status: typing_extensions.NotRequired[
        typing_extensions.Literal["available", "pending", "sold"]
    ]
    """
    pet status in the store
    """

    tags: typing_extensions.NotRequired[typing.List[Tag]]


class _SerializerPet(pydantic.BaseModel):
    """
    Serializer for Pet handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    category: typing.Optional[_SerializerCategory] = pydantic.Field(
        alias="category", default=None
    )
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    name: str = pydantic.Field(
        alias="name",
    )
    photo_urls: typing.List[str] = pydantic.Field(
        alias="photoUrls",
    )
    status: typing.Optional[
        typing_extensions.Literal["available", "pending", "sold"]
    ] = pydantic.Field(alias="status", default=None)
    tags: typing.Optional[typing.List[_SerializerTag]] = pydantic.Field(
        alias="tags", default=None
    )
