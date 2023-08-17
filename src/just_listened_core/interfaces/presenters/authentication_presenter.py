from abc import abstractmethod

from fastapi.responses import JSONResponse

from just_listened_core.domain.dtos import AuthenticateUserOutputDto
from just_listened_core.interfaces.presenters.base_presenter import BasePresenterInterface


class AuthenticationPresenterInterface(BasePresenterInterface):
    @abstractmethod
    def present_valid_token(self, output_dto: AuthenticateUserOutputDto) -> JSONResponse:
        """Present with valid token

        Args:
            token (AuthenticateUserOutputDto): AuthenticateUserOutputDto

        Returns:
            JSONResponse: JSONResponse
        """
        pass

    @abstractmethod
    def present_with_invalid_token(self) -> JSONResponse:
        """Present invalid token message

        Returns:
            JSONResponse: JSONResponse
        """
        pass
