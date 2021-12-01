"""New table

Revision ID: ec1a1cc7e4f8
Revises: 
Create Date: 2021-01-04 20:25:23.893759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec1a1cc7e4f8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('date', sa.Text(), nullable=True),
    sa.Column('disc', sa.Text(), nullable=True),
    sa.Column('d_url', sa.Text(), nullable=True),
    sa.Column('i_url', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game')
    # ### end Alembic commands ###
