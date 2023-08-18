from fastapi.responses import JSONResponse

from just_listened_core.domain.dtos import SearchSpotifyOutputDto
from just_listened_core.interfaces.presenters.base_presenter import BasePresenterInterface


class SpotifyPresenterInterface(BasePresenterInterface):
    def present_results(self, output_dto: SearchSpotifyOutputDto) -> JSONResponse:
        """Present the results found

        Args:
            output_dto (SearchSpotifyOutputDto): SearchSpotifyOutputDto

        Returns:
            JSONResponse: JSONResponse
        """
        pass
