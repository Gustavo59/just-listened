from fastapi import APIRouter, Response

from just_listened_core.controllers import AlbumController

router = APIRouter(prefix="/album", tags=["Album"])


@router.get(
    "/",
    response_class=Response,
)
def get_album(id: int = None, external_id: str = None):
    """Get Album

    Args:
        id (int, optional): Album id. Defaults to None.
        external_id (str, optional): Album external id. Defaults to None.

    Returns:
        dict: dict
    """
    controller = AlbumController()
    return controller.get_album(id=id, external_id=external_id)


@router.post(
    "/",
    response_class=Response,
)
def create_album(request: dict):
    """Create Album

    Args:
        album (GetAlbumInputDto): GetAlbumInputDto

    Returns:
        dict: dict
    """
    controller = AlbumController()
    return controller.create_album(request)
