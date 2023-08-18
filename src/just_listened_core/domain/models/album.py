from sqlalchemy import Column, Date, String

from just_listened_core.database import JustListenedCoreBaseModel


class Album(JustListenedCoreBaseModel):
    __tablename__ = "album"

    name = Column(String, nullable=False)
    external_id = Column(String, nullable=False, unique=True)
    image_url = Column(String, nullable=False)
    release_date = Column(Date, nullable=False)
