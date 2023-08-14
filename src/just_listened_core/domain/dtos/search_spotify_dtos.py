from pydantic import BaseModel


class AlbumSpotifyDto(BaseModel):
    id: str
    image_url: str
    name: str
    release_date: str
    release_date_precision: str
    artists_name: list[str]


class ArtistSpotifyDto(BaseModel):
    id: str
    genres: list[str]
    image_url: str
    name: str


class SearchSpotifyOutputDto(BaseModel):
    albums: list[AlbumSpotifyDto]
    artists: list[ArtistSpotifyDto]
