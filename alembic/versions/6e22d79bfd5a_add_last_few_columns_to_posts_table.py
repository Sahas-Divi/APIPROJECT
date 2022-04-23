"""add last few columns to posts table

Revision ID: 6e22d79bfd5a
Revises: b15a4c85f5d0
Create Date: 2022-04-18 15:48:54.264196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e22d79bfd5a'
down_revision = 'b15a4c85f5d0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts",sa.Column("published",sa.Boolean(),server_default = "TRUE",nullable = False))
    op.add_column("posts",sa.Column("created_at",sa.TIMESTAMP(timezone=True),nullable = False,server_default = sa.text("now()")))
    pass


def downgrade():
    op.drop_column("posts","published")
    op.drop_column("posts","created_at")
    pass
