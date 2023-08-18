from pydantic import ValidationError

from just_listened_core.database import session_scope
from just_listened_core.domain.dtos import CreateAlbumInputDto, GetAlbumInputDto
from just_listened_core.domain.exceptions import DataNotFoundError
from just_listened_core.presenter import AlbumPresenter
from just_listened_core.repositories import PostgresAlbumRepository
from just_listened_core.use_cases import CreateAlbum, GetAlbum


class AlbumController:
    def __init__(self):
        self._presenter = AlbumPresenter()

    def get_album(self, id: int = None, external_id: str = None):
        with session_scope() as session:
            album_repository = PostgresAlbumRepository(session)

            try:
                get_album_dto = GetAlbumInputDto(id=id, external_id=external_id)

                use_case = GetAlbum(album_repository=album_repository)

                output_dto = use_case.run(get_album_dto)
            except ValidationError as exc:
                return self._presenter.present_field_required(exc)
            except DataNotFoundError:
                return self._presenter.present_not_found()
            except Exception as exc:
                raise self._presenter.present_with_error(exc)

        return self._presenter.present_found(output_dto=output_dto)

    def create_album(self, request: dict):
        with session_scope() as session:
            album_repository = PostgresAlbumRepository(session)

            try:
                create_album_dto = CreateAlbumInputDto(**request)

                use_case = CreateAlbum(album_repository=album_repository, presenter=self._presenter)

                output_dto = use_case.run(create_album_dto)
            except ValidationError as exc:
                return self._presenter.present_field_required(exc)
            except Exception as exc:
                raise self._presenter.present_with_error(exc)

        return self._presenter.present_created(output_dto=output_dto)
