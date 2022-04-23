"""add foregin key to posts table

Revision ID: b15a4c85f5d0
Revises: 6c37eba7c922
Create Date: 2022-04-18 15:38:45.555642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b15a4c85f5d0'
down_revision = '6c37eba7c922'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id",sa.Integer(),nullable = False))
    op.create_foreign_key("posts_users_fkey",source_table="posts",referent_table="users",
    local_cols=["owner_id"],remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint("posts_users_fkey","posts")
    op.drop_column("posts","owner_id")
    pass
