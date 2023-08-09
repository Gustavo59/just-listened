import factory

from just_listened_core.domain.models import Album


class AlbumFactory(factory.Factory):
    class Meta:
        model = Album
