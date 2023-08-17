import logging

from just_listened_core.controllers import AuthenticationController
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


app.include_router(album.router)
