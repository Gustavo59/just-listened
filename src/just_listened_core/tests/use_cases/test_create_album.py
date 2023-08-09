import datetime

import pytest

from just_listened_core.domain.dtos import CreateAlbumInputDto
from just_listened_core.domain.models import Album
from just_listened_core.presenter import AlbumPresenter
from just_listened_core.repositories import PostgresAlbumRepository
from just_listened_core.use_cases import CreateAlbum


@pytest.fixture
def album_repository(db_session):
    return PostgresAlbumRepository(db_session)


@pytest.fixture
def use_case(album_repository):
    return CreateAlbum(album_repository=album_repository, presenter=AlbumPresenter())


@pytest.fixture
def input_dto():
    return CreateAlbumInputDto(
        name="To Pimp a Butterfly",
        external_id="7ycBtnsMtyVbbwTfJwRjSP",
        image_url="https://i.scdn.co/image/ab67616d0000b273cdb645498cd3d8a2db4d05e1",
        release_date="2015-03-16",
    )


def test_use_case_success(input_dto: CreateAlbumInputDto, use_case: CreateAlbum, db_session):
    response = use_case.run(input_dto)

    assert response.album.id == 1
    assert response.album.name == "To Pimp a Butterfly"
    assert response.album.external_id == "7ycBtnsMtyVbbwTfJwRjSP"
    assert response.album.image_url == "https://i.scdn.co/image/ab67616d0000b273cdb645498cd3d8a2db4d05e1"
    assert response.album.release_date == datetime.date(2015, 3, 16)

    album: Album | None = db_session.query(Album).one_or_none()

    assert album
    assert album.id == 1
    assert album.name == "To Pimp a Butterfly"
    assert album.external_id == "7ycBtnsMtyVbbwTfJwRjSP"
    assert album.image_url == "https://i.scdn.co/image/ab67616d0000b273cdb645498cd3d8a2db4d05e1"
    assert album.release_date == datetime.date(2015, 3, 16)
