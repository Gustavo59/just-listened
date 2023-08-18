import datetime

import pytest

from just_listened_core.domain.dtos import GetAlbumInputDto
from just_listened_core.domain.models import Album
from just_listened_core.repositories import PostgresAlbumRepository
from just_listened_core.use_cases import GetAlbum


@pytest.fixture
def album_repository(db_session):
    return PostgresAlbumRepository(db_session)


@pytest.fixture
def use_case(album_repository):
    return GetAlbum(album_repository=album_repository)


@pytest.fixture(autouse=True)
def database_populated(db_session):
    album = Album(
        name="To Pimp a Butterfly",
        external_id="7ycBtnsMtyVbbwTfJwRjSP",
        image_url="https://i.scdn.co/image/ab67616d0000b273cdb645498cd3d8a2db4d05e1",
        release_date="2015-03-16",
    )

    db_session.add(album)
    db_session.flush()


@pytest.fixture
def input_dto_with_id():
    return GetAlbumInputDto(id=1)


@pytest.fixture
def input_dto_with_external_id():
    return GetAlbumInputDto(external_id="7ycBtnsMtyVbbwTfJwRjSP")


def test_use_case_success(
    self_destructible_db,
    input_dto_with_id: GetAlbumInputDto,
    input_dto_with_external_id: GetAlbumInputDto,
    use_case: GetAlbum,
    db_session,
):
    response_with_id = use_case.run(input_dto_with_id)

    assert response_with_id.album.id == 1
    assert response_with_id.album.name == "To Pimp a Butterfly"
    assert response_with_id.album.external_id == "7ycBtnsMtyVbbwTfJwRjSP"
    assert response_with_id.album.image_url == "https://i.scdn.co/image/ab67616d0000b273cdb645498cd3d8a2db4d05e1"
    assert response_with_id.album.release_date == datetime.date(2015, 3, 16)

    response_with_external_id = use_case.run(input_dto_with_external_id)

    assert response_with_external_id.album.id == 1
    assert response_with_external_id.album.name == "To Pimp a Butterfly"
    assert response_with_external_id.album.external_id == "7ycBtnsMtyVbbwTfJwRjSP"
    assert (
        response_with_external_id.album.image_url == "https://i.scdn.co/image/ab67616d0000b273cdb645498cd3d8a2db4d05e1"
    )
    assert response_with_external_id.album.release_date == datetime.date(2015, 3, 16)
