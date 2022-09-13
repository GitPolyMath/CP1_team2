"""empty message

Revision ID: 4dde4414dc88
Revises: 73ed0f78ec1c
Create Date: 2022-09-08 05:35:30.033736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4dde4414dc88'
down_revision = '73ed0f78ec1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fridge',
    sa.Column('product', sa.String(length=120), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('barcode', sa.Integer(), nullable=True),
    sa.Column('subclass', sa.String(length=150), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.Column('old_exp_date', sa.Date(), nullable=False),
    sa.Column('new_exp_date', sa.Date(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('modify_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_fridge_user_id_user'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('product', name=op.f('pk_fridge'))
    )
    op.add_column('user', sa.Column('gender', sa.String(length=100), server_default='F', nullable=True))
    op.add_column('user', sa.Column('region', sa.String(length=200), server_default='서울', nullable=True))
    op.add_column('user', sa.Column('age', sa.Integer(), server_default='30', nullable=True))
    op.add_column('user', sa.Column('create_date', sa.DateTime(), server_default='2022-09-15 19:27:35.508', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'create_date')
    op.drop_column('user', 'age')
    op.drop_column('user', 'region')
    op.drop_column('user', 'gender')
    op.drop_table('fridge')
    # ### end Alembic commands ###
