import logging

from fastapi_login import LoginManager

from just_listened_core.domain.dtos import AuthenticateUserInputDto
from just_listened_core.domain.exceptions import UserInvalidToken
from just_listened_core.presenter import AuthenticationPresenter
from just_listened_core.services import GoogleOAuthService
from just_listened_core.use_cases import Authentication

LOGGER = logging.getLogger(__name__)


class AuthenticationController:
    def __init__(self, login_manager: LoginManager):
        self._login_manager = login_manager
        self._presenter = AuthenticationPresenter()

    def run(self, request: dict):
        try:
            authenticate_user_dto = AuthenticateUserInputDto(**request)
            use_case = Authentication(login_manager=self._login_manager, oauth_service=GoogleOAuthService())
            output_dto = use_case.run(input_dto=authenticate_user_dto)
            return self._presenter.present_valid_token(output_dto=output_dto)
        except UserInvalidToken:
            return self._presenter.present_with_invalid_token()
        except Exception as exc:
            LOGGER.exception(exc)
            return self._presenter.present_with_error(message="Unexpected erro while authenticating user")
