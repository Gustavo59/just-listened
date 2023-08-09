""" Create album table

Revision ID: 114ea2ead835
Revises:
Create Date: 2023-08-09 12:38:52.250566

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "114ea2ead835"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "album",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("external_id", sa.String(), nullable=False),
        sa.Column("image_url", sa.String(), nullable=False),
        sa.Column("release_date", sa.Date(), nullable=False),
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_album")),
        sa.UniqueConstraint("external_id", name=op.f("uq_album_external_id")),
    )


def downgrade() -> None:
    op.drop_table("album")
