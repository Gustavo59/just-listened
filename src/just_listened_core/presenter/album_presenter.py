from fastapi import status
from fastapi.responses import JSONResponse

from just_listened_core.domain.dtos import CreateAlbumOutputDto, GetAlbumOutputDto
from just_listened_core.domain.models import Album
from just_listened_core.interfaces.presenters import AlbumPresenterInterface
from just_listened_core.presenter.base_presenter import BasePresenter


class AlbumPresenter(AlbumPresenterInterface, BasePresenter):
    def present_found(self, output_dto: GetAlbumOutputDto) -> JSONResponse:
        """Present the album found

        Args:
            output_dto (GetAlbumOutputDto): GetAlbumOutputDto

        Returns:
            JSONResponse: JSONResponse
        """
        return JSONResponse(
            content={"message": "Album found successfully", "album": self._album_to_dict(output_dto.album)},
            status_code=status.HTTP_200_OK,
        )

    def present_not_found(self) -> JSONResponse:
        """Present album not found

        Returns:
            JSONResponse: JSONResponse
        """
        return JSONResponse(content={"message": "Album not found"}, status_code=status.HTTP_404_NOT_FOUND)

    def present_created(self, output_dto: CreateAlbumOutputDto) -> JSONResponse:
        """Presente the CreateAlbum

        Args:
            output_dto (CreateAlbumOutputDto): CreateAlbumOutputDto

        Returns:
            JSONResponse: JSONResponse
        """
        return JSONResponse(
            content={"message": "Album created successfully", "album": self._album_to_dict(output_dto.album)},
            status_code=status.HTTP_200_OK,
        )

    def _album_to_dict(self, album: Album):
        return {
            "album_id": album.id,
            "name": album.name,
            "external_id": album.external_id,
            "image_url": album.image_url,
            "release_date": str(album.release_date),
        }
