import logging

from just_listened_core.external_interfaces.just_listened_api.dependencies import app_factory
from just_listened_core.external_interfaces.just_listened_api.routers import album

LOGGER = logging.getLogger(__name__)

app = app_factory(title="Just Listened")


@app.get("/health", include_in_schema=False)
def health():
    return {"message": "OK"}


app.include_router(album.router)
