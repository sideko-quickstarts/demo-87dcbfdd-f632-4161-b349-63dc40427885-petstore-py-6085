import pydantic
import typing


class ApiResponse(pydantic.BaseModel):
    """
    ApiResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    code: typing.Optional[int] = pydantic.Field(alias="code", default=None)
    message: typing.Optional[str] = pydantic.Field(alias="message", default=None)
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
