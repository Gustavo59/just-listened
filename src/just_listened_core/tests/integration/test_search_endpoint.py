import pytest

from just_listened_core.services import SpotifyService
from just_listened_core.tests.data.mocks import SPOTIFY_INVALID_TOKEN
from just_listened_core.tests.dataloader import DataLoader

rout_uri = "/search"


@pytest.fixture
def spotify_search_result_mock(mocker):
    mocker.patch.object(SpotifyService, "search", return_value=DataLoader.SPOTIFY_SEARCH_RESULT.from_json())


@pytest.fixture
def spotify_search_connection_error_mock(mocker):
    mocker.patch.object(SpotifyService, "search", return_value=SPOTIFY_INVALID_TOKEN)


def test_endpoint_sucess(client, spotify_search_result_mock):
    response = client.get(f"{rout_uri}?query=to+pimp+a+butterfly")

    assert response.status_code == 200
    assert response.json()["message"] == "Search done successfully"
    assert response.json()["results"]["albums"][0] == {
        "id": "7ycBtnsMtyVbbwTfJwRjSP",
        "image_url": "https://i.scdn.co/image/ab67616d0000b273cdb645498cd3d8a2db4d05e1",
        "name": "To Pimp A Butterfly",
        "release_date": "2015-03-16",
        "release_date_precision": "day",
        "artists_name": ["Kendrick Lamar"],
    }


def test_endpoint_spotify_connection_error(client, spotify_search_connection_error_mock):
    response = client.get(f"{rout_uri}?query=to+pimp+a+butterfly")

    assert response.status_code == 401
    assert response.json()["message"] == "Error while connecting to Spotify API. Invalid access token"
