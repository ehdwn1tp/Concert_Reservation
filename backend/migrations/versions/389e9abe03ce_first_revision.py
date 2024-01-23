"""first revision

Revision ID: 389e9abe03ce
Revises: 
Create Date: 2024-01-19 05:25:00.469182

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '389e9abe03ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Table1',
    sa.Column('Col_1', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Col_2', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('Col_1')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Table1')
    # ### end Alembic commands ###
