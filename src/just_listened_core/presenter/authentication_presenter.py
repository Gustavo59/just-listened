from fastapi import status
from fastapi.responses import JSONResponse

from just_listened_core.domain.dtos.authenticate_user_dtos import AuthenticateUserOutputDto
from just_listened_core.presenter.base_presenter import BasePresenter


class AuthenticationPresenter(BasePresenter):
    def present_valid_token(self, output_dto: AuthenticateUserOutputDto) -> JSONResponse:
        """Present with valid token

        Args:
            token (AuthenticateUserOutputDto): AuthenticateUserOutputDto

        Returns:
            JSONResponse: JSONResponse
        """
        return JSONResponse(
            content={"message": "User authenticated successfully", "token": output_dto.access_token},
            status_code=status.HTTP_200_OK,
        )

    def present_with_invalid_token(self) -> JSONResponse:
        """Present invalid token message

        Returns:
            JSONResponse: JSONResponse
        """
        return JSONResponse(content={"message": "Invalid token"}, status_code=status.HTTP_401_UNAUTHORIZED)
