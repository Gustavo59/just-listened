from abc import abstractmethod

from fastapi.responses import JSONResponse

from just_listened_core.domain.dtos import CreateAlbumOutputDto, GetAlbumOutputDto
from just_listened_core.interfaces.presenters.base_presenter import BasePresenterInterface


class AlbumPresenterInterface(BasePresenterInterface):
    @abstractmethod
    def present_found(self, output_dto: GetAlbumOutputDto) -> JSONResponse:
        """Present the album found

        Args:
            output_dto (GetAlbumOutputDto): GetAlbumOutputDto

        Returns:
            dict: dict
        """
        pass

    @abstractmethod
    def present_not_found(self) -> JSONResponse:
        """Present album not found

        Returns:
            dict: dict
        """
        pass

    @abstractmethod
    def present_created(self, output_dto: CreateAlbumOutputDto) -> JSONResponse:
        """Presente the Album created

        Args:
            output_dto (CreateAlbumOutputDto): CreateAlbumOutputDto

        Returns:
            dict: Album as dict
        """
        pass
