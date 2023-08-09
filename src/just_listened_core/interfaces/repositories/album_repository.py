from abc import ABC, abstractmethod

from just_listened_core.domain.dtos import CreateAlbumInputDto, GetAlbumInputDto
from just_listened_core.domain.models import Album


class AlbumRepositoryInterface(ABC):
    @abstractmethod
    def get(self, get_album_dto: GetAlbumInputDto) -> Album | None:
        """Get an Album by id or external id

        Args:
            get_album_dto (GetAlbumInputDto): GetAlbumInputDto

        Returns:
            Album: Album
        """
        pass

    @abstractmethod
    def create(self, create_album_dto: CreateAlbumInputDto) -> Album:
        """Create an Album

        Args:
            create_album_dto (CreateAlbumInputDto): CreateAlbumInputDto

        Returns:
            Album: Album
        """
        pass
