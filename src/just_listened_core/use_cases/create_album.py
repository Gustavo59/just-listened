from just_listened_core.domain.dtos import CreateAlbumInputDto, CreateAlbumOutputDto
from just_listened_core.interfaces.presenters import AlbumPresenterInterface
from just_listened_core.interfaces.repositories import AlbumRepositoryInterface


class CreateAlbum:
    def __init__(self, album_repository: AlbumRepositoryInterface, presenter: AlbumPresenterInterface):
        self._album_repository = album_repository
        self._presenter = presenter

    def run(self, input_dto: CreateAlbumInputDto):
        album = self._album_repository.create(create_album_dto=input_dto)
        output_dto = CreateAlbumOutputDto(album=album)
        return output_dto
