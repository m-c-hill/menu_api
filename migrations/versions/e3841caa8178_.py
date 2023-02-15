"""empty message

Revision ID: e3841caa8178
Revises: 
Create Date: 2023-02-15 10:53:37.802049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e3841caa8178"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "customer",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "dish",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("price", sa.Float(), nullable=True),
        sa.Column(
            "hot_or_cold", sa.Enum("hot", "cold", name="temperatureenum"), nullable=True
        ),
        sa.Column(
            "category",
            sa.Enum(
                "starters",
                "mains",
                "specials",
                "sides",
                "desserts",
                "drinks",
                name="categoryenum",
            ),
            nullable=True,
        ),
        sa.Column("ingredients", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "order",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("customer_id", sa.Integer(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("(CURRENT_TIMESTAMP)"),
            nullable=True,
        ),
        sa.Column("total_price", sa.Float(), nullable=True),
        sa.Column("payment_complete", sa.Boolean(), nullable=True),
        sa.Column("order_fulfilled", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ["customer_id"],
            ["customer.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "order_item",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("order_id", sa.Integer(), nullable=True),
        sa.Column("quantity", sa.Integer(), nullable=True),
        sa.Column("price", sa.Float(), nullable=True),
        sa.Column("dish_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["dish_id"],
            ["dish.id"],
        ),
        sa.ForeignKeyConstraint(
            ["order_id"],
            ["order.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("order_item")
    op.drop_table("order")
    op.drop_table("dish")
    op.drop_table("customer")
    # ### end Alembic commands ###
