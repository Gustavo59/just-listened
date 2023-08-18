from abc import ABC, abstractmethod

from just_listened_core.domain.dtos import SearchSpotifyOutputDto


class SpotifyServiceInterface(ABC):
    @abstractmethod
    def search(self, query: str) -> list[SearchSpotifyOutputDto]:
        """Search

        Args:
            query (str): Query search

        Returns:
            list: list
        """
        pass
