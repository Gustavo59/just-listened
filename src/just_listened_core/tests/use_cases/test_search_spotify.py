import pytest

from just_listened_core.domain.exceptions import SpotifyConnectionError
from just_listened_core.services import SpotifyService
from just_listened_core.tests.data.mocks import SPOTIFY_INVALID_TOKEN
from just_listened_core.tests.dataloader import DataLoader
from just_listened_core.use_cases import SearchSpotify


@pytest.fixture
def spotify_service():
    return SpotifyService()


@pytest.fixture
def use_case(spotify_service):
    return SearchSpotify(spotify_service=spotify_service)


@pytest.fixture
def spotify_search_result_mock(mocker):
    mocker.patch.object(SpotifyService, "search", return_value=DataLoader.SPOTIFY_SEARCH_RESULT.from_json())


@pytest.fixture
def spotify_search_unauthorized_error_mock(mocker):
    mocker.patch.object(SpotifyService, "search", return_value=SPOTIFY_INVALID_TOKEN)


def test_use_case_success(use_case, spotify_search_result_mock):
    response = use_case.run("to pimp a butterfly")

    assert response
    assert len(response.albums) == 20
    assert len(response.artists) == 0

    assert response.albums[0].id == "7ycBtnsMtyVbbwTfJwRjSP"
    assert response.albums[0].name == "To Pimp A Butterfly"
    assert response.albums[0].image_url == "https://i.scdn.co/image/ab67616d0000b273cdb645498cd3d8a2db4d05e1"
    assert response.albums[0].release_date == "2015-03-16"
    assert response.albums[0].release_date_precision == "day"
    assert response.albums[0].artists_name == ["Kendrick Lamar"]


def test_use_case_connection_error(use_case, spotify_search_unauthorized_error_mock):
    with pytest.raises(SpotifyConnectionError):
        use_case.run("to pimp a butterfly")
