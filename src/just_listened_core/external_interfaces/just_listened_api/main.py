import logging

from fastapi import Response

from just_listened_core.controllers import AuthenticationController, SpotifyController
from just_listened_core.external_interfaces.just_listened_api import app_factory, login_manager
from just_listened_core.external_interfaces.just_listened_api.routers import album

LOGGER = logging.getLogger(__name__)

app = app_factory(title="Just Listened")


@app.get("/health", include_in_schema=False)
def health():
    return {"message": "OK"}


@app.post("/auth", tags=["Authentication"])
def authentication(request: dict):
    controller = AuthenticationController(login_manager=login_manager)
    return controller.run(request)


@app.get(
    "/search",
    response_class=Response,
)
def search(query: str):
    """Search

    Args:
        query (str): Query search.

    Returns:
        dict: dict
    """
    controller = SpotifyController()
    return controller.search(query)


app.include_router(album.router)
