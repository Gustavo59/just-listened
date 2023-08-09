import pytest

from just_listened_core.domain.models import Album

route_uri = "/album"


@pytest.fixture
def database_populated(db_session):
    album = Album(
        name="To Pimp a Butterfly",
        external_id="7ycBtnsMtyVbbwTfJwRjSP",
        image_url="https://i.scdn.co/image/ab67616d0000b273cdb645498cd3d8a2db4d05e1",
        release_date="2015-03-16",
    )

    db_session.add(album)
    db_session.commit()


def test_endpoint_success(self_destructible_db, database_populated, client):
    album_id = 1

    response = client.get(f"{route_uri}?id={album_id}")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Album found successfully",
        "album": {
            "album_id": 1,
            "name": "To Pimp a Butterfly",
            "external_id": "7ycBtnsMtyVbbwTfJwRjSP",
            "image_url": "https://i.scdn.co/image/ab67616d0000b273cdb645498cd3d8a2db4d05e1",
            "release_date": "2015-03-16",
        },
    }

    album_external_id = "7ycBtnsMtyVbbwTfJwRjSP"

    response = client.get(f"{route_uri}?external_id={album_external_id}")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Album found successfully",
        "album": {
            "album_id": 1,
            "name": "To Pimp a Butterfly",
            "external_id": "7ycBtnsMtyVbbwTfJwRjSP",
            "image_url": "https://i.scdn.co/image/ab67616d0000b273cdb645498cd3d8a2db4d05e1",
            "release_date": "2015-03-16",
        },
    }


def test_endpoint_not_found(client):
    album_id = 9999

    response = client.get(f"{route_uri}?id={album_id}")

    assert response.status_code == 404
    assert response.json() == {"message": "Album not found"}


def test_endpoint_invalid_parameters(client):
    response = client.get(f"{route_uri}?invalid_parameter=1")

    assert response.status_code == 400
    assert response.json() == {
        "message": "Validation error on request body",
        "missing_fields": [],
        "invalid_fields": {"": "Value error, One of id or external_id must be filled"},
    }
