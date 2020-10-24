"""empty message

Revision ID: 0059e4ddbc8d
Revises: d8e343a4e450
Create Date: 2020-10-23 23:18:51.086939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0059e4ddbc8d'
down_revision = 'd8e343a4e450'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Show', 'date')
    # ### end Alembic commands ###
