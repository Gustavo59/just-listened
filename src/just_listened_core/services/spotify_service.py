from urllib.parse import urljoin

import requests

from just_listened_core.domain.dtos.search_spotify_dtos import SearchSpotifyOutputDto
from just_listened_core.interfaces.services import SpotifyServiceInterface
from just_listened_core.settings import get_spotify_settings


class SpotifyService(SpotifyServiceInterface):
    def __init__(self):
        self._settings = get_spotify_settings()
        self._spotify_api_url = self._settings.SPOTIFY_API_URL

    def _get_access_token(self):
        url = "https://accounts.spotify.com/api/token"

        data = {
            "grant_type": "client_credentials",
            "client_id": self._settings.SPOTIFY_CLIENT_ID,
            "client_secret": self._settings.SPOTIFY_CLIENT_SECRET,
        }

        auth_response = requests.post(url, data=data)

        return auth_response.json().get("access_token")

    def _get_headers(self):
        return {"Authorization": f"Bearer {self._get_access_token()}"}

    def search(self, query: str) -> list[SearchSpotifyOutputDto]:
        q = query.replace(" ", "+")
        url = urljoin(self._spotify_api_url, f"search?q={q}&type=album%2Cartist")

        response = requests.get(url, headers=self._get_headers())

        return response.json()
