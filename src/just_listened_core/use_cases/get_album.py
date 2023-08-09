from just_listened_core.domain.dtos import GetAlbumInputDto, GetAlbumOutputDto
from just_listened_core.domain.exceptions import DataNotFoundError
from just_listened_core.interfaces.presenters import AlbumPresenterInterface
from just_listened_core.interfaces.repositories import AlbumRepositoryInterface


class GetAlbum:
    def __init__(self, album_repository: AlbumRepositoryInterface, presenter: AlbumPresenterInterface):
        self._album_repository = album_repository
        self._presenter = presenter

    def run(self, input_dto: GetAlbumInputDto):
        try:
            album = self._album_repository.get(get_album_dto=input_dto)
            output_dto = GetAlbumOutputDto(album=album)
            return output_dto
        except DataNotFoundError as e:
            raise e
