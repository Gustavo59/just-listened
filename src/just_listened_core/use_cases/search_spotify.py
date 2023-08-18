from just_listened_core.domain.dtos import SearchSpotifyOutputDto, AlbumSpotifyDto, ArtistSpotifyDto
from just_listened_core.domain.exceptions import SpotifyConnectionError
from just_listened_core.interfaces.services import SpotifyServiceInterface


class SearchSpotify:
    def __init__(self, spotify_service: SpotifyServiceInterface):
        self._spotify_service = spotify_service

    def run(self, query: str) -> SearchSpotifyOutputDto:
        try:
            response = self._spotify_service.search(query)

            if response.get("error"):
                raise SpotifyConnectionError(
                    message=response.get("error").get("message"), http_status=response.get("error").get("http_status")
                )

            output_dto = SearchSpotifyOutputDto(
                albums=self._format_albums(response.get("albums").get("items")),
                artists=self._format_artists(response.get("artists").get("items")),
            )
            return output_dto
        except Exception as e:
            raise e

    def _format_albums(self, albums: list[dict]) -> list[AlbumSpotifyDto]:
        return [
            AlbumSpotifyDto(
                id=a.get("id"),
                image_url=a.get("images")[0].get("url") if len(a.get("images")) > 1 else "",
                name=a.get("name"),
                release_date=a.get("release_date"),
                release_date_precision=a.get("release_date_precision"),
                artists_name=[artist.get("name") for artist in a.get("artists")],
            )
            for a in albums
        ]

    def _format_artists(self, artists: list[dict]) -> list[ArtistSpotifyDto]:
        return [
            ArtistSpotifyDto(
                id=a.get("id"),
                genres=a.get("genres"),
                image_url=a.get("images")[0].get("url") if len(a.get("images")) > 1 else "",
                name=a.get("name"),
            )
            for a in artists
        ]
