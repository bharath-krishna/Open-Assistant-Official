"""Add chat data opt out field

Revision ID: 401eef162771
Revises: b66fd8f9da1f
Create Date: 2023-04-24 21:30:19.947411

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "401eef162771"
down_revision = "b66fd8f9da1f"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("chat", sa.Column("allow_data_use", sa.Boolean(), server_default=sa.text("true"), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("chat", "allow_data_use")
    # ### end Alembic commands ###
