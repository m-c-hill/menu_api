"""empty message

Revision ID: db12c496b197
Revises: 
Create Date: 2023-02-15 09:05:17.586522

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "db12c496b197"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("github_login", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("avatar", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("github_login"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    # ### end Alembic commands ###