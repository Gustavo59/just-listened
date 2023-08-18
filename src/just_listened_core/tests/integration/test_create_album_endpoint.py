import datetime

import pytest

from just_listened_core.domain.models import Album

route_uri = "/album"


@pytest.fixture
def body_mock():
    return {
        "name": "To Pimp a Butterfly",
        "external_id": "7ycBtnsMtyVbbwTfJwRjSP",
        "image_url": "https://i.scdn.co/image/ab67616d0000b273cdb645498cd3d8a2db4d05e1",
        "release_date": "2015-03-16",
    }


@pytest.fixture
def invalid_body_mock():
    return {
        "name": "To Pimp a Butterfly",
        "image_url": "https://i.scdn.co/image/ab67616d0000b273cdb645498cd3d8a2db4d05e1",
        "release_date": "2015-03-16",
    }


def test_endpoint_success(self_destructible_db, body_mock, client, db_session):
    response = client.post(f"{route_uri}", json=body_mock)

    assert response.status_code == 200
    assert response.json() == {
        "message": "Album created successfully",
        "album": {
            "album_id": 1,
            "name": "To Pimp a Butterfly",
            "external_id": "7ycBtnsMtyVbbwTfJwRjSP",
            "image_url": "https://i.scdn.co/image/ab67616d0000b273cdb645498cd3d8a2db4d05e1",
            "release_date": "2015-03-16",
        },
    }

    album: Album | None = db_session.query(Album).one_or_none()

    assert album
    assert album.id == 1
    assert album.name == "To Pimp a Butterfly"
    assert album.external_id == "7ycBtnsMtyVbbwTfJwRjSP"
    assert album.image_url == "https://i.scdn.co/image/ab67616d0000b273cdb645498cd3d8a2db4d05e1"
    assert album.release_date == datetime.date(2015, 3, 16)


def test_endpoint_invalid_body(self_destructible_db, invalid_body_mock, client, db_session):
    response = client.post(f"{route_uri}", json=invalid_body_mock)

    assert response.status_code == 400
    assert response.json() == {
        "message": "Validation error on request body",
        "missing_fields": ["external_id"],
        "invalid_fields": {},
    }
