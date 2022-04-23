"""add content column to posts table

Revision ID: 0f8ddffa5bca
Revises: 2a0ff8dfc74d
Create Date: 2022-04-18 15:23:25.165263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f8ddffa5bca'
down_revision = '2a0ff8dfc74d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts",sa.Column("content",sa.String(),nullable = False))
    pass


def downgrade():
    op.drop_column("posts","content")
    pass
