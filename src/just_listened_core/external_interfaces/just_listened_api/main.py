import logging

from src.just_listened_core.external_interfaces.just_listened_api.dependencies import app_factory

LOGGER = logging.getLogger(__name__)

app = app_factory(title="Just Listened")


@app.get("/health", include_in_schema=False)
def health():
    return {"message": "OK"}
