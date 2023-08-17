import pytest

from just_listened_core.services.google_oauth_service import GoogleOAuthService
from just_listened_core.tests.dataloader import DataLoader


@pytest.fixture
def google_verify_token_result_mock(mocker):
    mocker.patch.object(
        GoogleOAuthService, "verify_token", return_value=DataLoader.OAUTH_VERIFY_TOKEN_RESPONSE.from_json()
    )


def test_authentication_success(client, google_verify_token_result_mock):
    data = {"id_token": "TOKEN_TEST"}
    response = client.post("/auth", json=data)

    assert response.status_code == 200
    assert "token" in response.json().keys()


def test_authentication_with_invalid_token(client):
    data = {"id_token": "token"}
    response = client.post("/auth", json=data)

    assert response.status_code == 401
    assert response.json() == {"message": "Invalid token"}
