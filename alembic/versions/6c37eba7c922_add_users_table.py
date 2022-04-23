"""add users table

Revision ID: 6c37eba7c922
Revises: 0f8ddffa5bca
Create Date: 2022-04-18 15:28:42.809745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c37eba7c922'
down_revision = '0f8ddffa5bca'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users",
    sa.Column("id",sa.Integer(),nullable = False),
    sa.Column("email",sa.String(),nullable=False),
    sa.Column("password",sa.String(),nullable = False),
    sa.Column("created_at",sa.TIMESTAMP(timezone=True),server_default = sa.text("now()"),nullable = False),
    sa.PrimaryKeyConstraint("id"),
    sa.UniqueConstraint("email")
    )
    pass


def downgrade():
    op.drop_table("users")
    pass
