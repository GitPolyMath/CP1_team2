"""empty message

Revision ID: 764dcb165d05
Revises: cc901481b762
Create Date: 2022-09-08 03:39:10.518230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '764dcb165d05'
down_revision = 'cc901481b762'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('create_date', sa.DateTime(), server_default='00:00:00', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'create_date')
    # ### end Alembic commands ###
