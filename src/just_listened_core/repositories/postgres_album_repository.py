from sqlalchemy.exc import NoResultFound

from just_listened_core.domain.dtos import CreateAlbumInputDto, GetAlbumInputDto
from just_listened_core.domain.exceptions import DataNotFoundError
from just_listened_core.domain.models import Album
from just_listened_core.interfaces.repositories import AlbumRepositoryInterface


class PostgresAlbumRepository(AlbumRepositoryInterface):
    def __init__(self, session) -> None:
        self._session = session

    def get(self, get_album_dto: GetAlbumInputDto) -> Album:
        album = self._session.query(Album)

        if get_album_dto.id:
            album = album.filter(Album.id == get_album_dto.id)
        elif get_album_dto.external_id:
            album = album.filter(Album.external_id == get_album_dto.external_id)
        try:
            return album.one()
        except NoResultFound:
            raise DataNotFoundError()

    def create(self, create_album_dto: CreateAlbumInputDto) -> Album:
        album = Album(
            name=create_album_dto.name,
            external_id=create_album_dto.external_id,
            image_url=create_album_dto.image_url,
            release_date=create_album_dto.release_date,
        )
        self._session.add(album)
        self._session.flush()
        return album
