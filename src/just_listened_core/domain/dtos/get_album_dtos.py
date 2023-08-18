from pydantic import BaseModel, model_validator

from just_listened_core.domain.models import Album


class GetAlbumInputDto(BaseModel):
    id: int | None = None
    external_id: str | None = None

    @model_validator(mode="before")
    def any_of(cls, values):
        if not any(values.values()):
            raise ValueError("One of id or external_id must be filled")
        return values


class GetAlbumOutputDto(BaseModel):
    album: Album

    class Config:
        arbitrary_types_allowed = True
