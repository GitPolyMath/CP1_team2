"""empty message

Revision ID: 19b71b08abde
Revises: 5d4de0310a9d
Create Date: 2022-09-06 01:46:22.355175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19b71b08abde'
down_revision = '5d4de0310a9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(op.f('fk_question_user_id_user'), 'question', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_question_user_id_user'), 'question', type_='foreignkey')
    op.drop_column('question', 'user_id')
    # ### end Alembic commands ###
