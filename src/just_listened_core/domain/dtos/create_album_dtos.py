from datetime import date

from pydantic import BaseModel

from just_listened_core.domain.models import Album


class CreateAlbumInputDto(BaseModel):
    name: str
    external_id: str
    image_url: str
    release_date: date


class CreateAlbumOutputDto(BaseModel):
    album: Album

    class Config:
        arbitrary_types_allowed = True
