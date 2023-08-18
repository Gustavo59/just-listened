from fastapi import status
from fastapi.responses import JSONResponse

from just_listened_core.domain.dtos import SearchSpotifyOutputDto
from just_listened_core.presenter.base_presenter import BasePresenter


class SpotifyPresenter(BasePresenter):
    def present_results(self, output_dto: SearchSpotifyOutputDto) -> JSONResponse:
        """Present the results found

        Args:
            output_dto (SearchSpotifyOutputDto): SearchSpotifyOutputDto

        Returns:
            JSONResponse: JSONResponse
        """
        return JSONResponse(
            content={"message": "Search done successfully", "results": self._result_to_dict(output_dto)},
            status_code=status.HTTP_200_OK,
        )

    def _result_to_dict(self, search_output_dto: SearchSpotifyOutputDto) -> dict:
        return {
            "albums": [a.model_dump() for a in search_output_dto.albums],
            "artists": [a.model_dump() for a in search_output_dto.artists],
        }
