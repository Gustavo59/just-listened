from just_listened_core.presenter import SpotifyPresenter
from just_listened_core.services import SpotifyService
from just_listened_core.use_cases import SearchSpotify


class SpotifyController:
    def __init__(self):
        self._presenter = SpotifyPresenter()

    def search(self, query: str):
        try:
            spotify_service = SpotifyService()

            use_case = SearchSpotify(spotify_service=spotify_service)

            output_dto = use_case.run(query)
        except Exception as exc:
            return self._presenter.present_with_error(exc)

        return self._presenter.present_results(output_dto=output_dto)
