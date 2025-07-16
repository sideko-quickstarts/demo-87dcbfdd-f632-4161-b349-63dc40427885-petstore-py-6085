import pydantic
import typing
import typing_extensions

from .category import Category
from .tag import Tag


class Pet(pydantic.BaseModel):
    """
    Pet
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    category: typing.Optional[Category] = pydantic.Field(alias="category", default=None)
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
    """
    pet status in the store
    """
    tags: typing.Optional[typing.List[Tag]] = pydantic.Field(alias="tags", default=None)
