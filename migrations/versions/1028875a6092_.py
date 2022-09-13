"""empty message

Revision ID: 1028875a6092
Revises: 3793ccd26d82
Create Date: 2022-09-08 21:15:26.477768

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1028875a6092'
down_revision = '3793ccd26d82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Barcode_categories',
    sa.Column('b_category_id', sa.Integer(), nullable=False),
    sa.Column('b_category_name', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('b_category_id', name=op.f('pk_Barcode_categories')),
    sa.UniqueConstraint('b_category_name', name=op.f('uq_Barcode_categories_b_category_name'))
    )
    op.create_table('Barcode_companies',
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('company_name', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('company_id', name=op.f('pk_Barcode_companies')),
    sa.UniqueConstraint('company_name', name=op.f('uq_Barcode_companies_company_name'))
    )
    op.create_table('Ingredient',
    sa.Column('ingredient_id', sa.Integer(), nullable=False),
    sa.Column('ingredient_name', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('ingredient_id', name=op.f('pk_Ingredient')),
    sa.UniqueConstraint('ingredient_name', name=op.f('uq_Ingredient_ingredient_name'))
    )
    op.create_table('Recipes',
    sa.Column('recipe_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('recipe_name', sa.String(length=200), nullable=False),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('recommand', sa.Integer(), nullable=True),
    sa.Column('scrap', sa.Integer(), nullable=True),
    sa.Column('cooking_serving', sa.Integer(), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('cooking_time', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('recipe_id', name=op.f('pk_Recipes'))
    )
    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('gender', sa.String(length=100), nullable=False),
    sa.Column('region', sa.String(length=200), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_User')),
    sa.UniqueConstraint('email', name=op.f('uq_User_email')),
    sa.UniqueConstraint('username', name=op.f('uq_User_username'))
    )
    op.create_table('Barcode',
    sa.Column('barcode_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('barcode', sa.Integer(), nullable=True),
    sa.Column('b_category_id', sa.Integer(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('product', sa.String(length=120), nullable=True),
    sa.Column('shelf_life', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['b_category_id'], ['Barcode_categories.b_category_id'], name=op.f('fk_Barcode_b_category_id_Barcode_categories')),
    sa.ForeignKeyConstraint(['company_id'], ['Barcode_companies.company_id'], name=op.f('fk_Barcode_company_id_Barcode_companies')),
    sa.ForeignKeyConstraint(['product'], ['Ingredient.ingredient_name'], name=op.f('fk_Barcode_product_Ingredient')),
    sa.PrimaryKeyConstraint('barcode_id', name=op.f('pk_Barcode')),
    sa.UniqueConstraint('barcode', name=op.f('uq_Barcode_barcode'))
    )
    op.create_table('Fridge',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('product', sa.String(length=200), nullable=True),
    sa.Column('barcode', sa.Integer(), nullable=True),
    sa.Column('subclass', sa.String(length=150), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.Column('exp_date', sa.Date(), nullable=False),
    sa.Column('adding_date', sa.DateTime(), nullable=True),
    sa.Column('modify_date', sa.DateTime(), nullable=True),
    sa.Column('remain_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['product'], ['Ingredient.ingredient_name'], name=op.f('fk_Fridge_product_Ingredient')),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], name=op.f('fk_Fridge_user_id_User'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_Fridge'))
    )
    op.create_table('Recipe_ingredient',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['recipe_id'], ['Recipes.recipe_id'], name=op.f('fk_Recipe_ingredient_recipe_id_Recipes')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_Recipe_ingredient'))
    )
    op.create_table('Recipe_situation',
    sa.Column('situation_id', sa.Integer(), nullable=False),
    sa.Column('reciepe_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['reciepe_id'], ['Recipes.recipe_id'], name=op.f('fk_Recipe_situation_reciepe_id_Recipes')),
    sa.PrimaryKeyConstraint('situation_id', name=op.f('pk_Recipe_situation'))
    )
    op.create_table('situation',
    sa.Column('situation_id', sa.Integer(), nullable=False),
    sa.Column('situation_name', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['situation_id'], ['Recipe_situation.situation_id'], name=op.f('fk_situation_situation_id_Recipe_situation')),
    sa.PrimaryKeyConstraint('situation_id', name=op.f('pk_situation'))
    )
    op.drop_table('barcode__categories')
    op.drop_table('fridge')
    op.drop_table('user')
    op.drop_constraint('uq_answer_user_id', 'answer', type_='unique')
    op.drop_constraint('fk_answer_question_id_question', 'answer', type_='foreignkey')
    op.drop_constraint('fk_answer_user_id_user', 'answer', type_='foreignkey')
    op.create_foreign_key(op.f('fk_answer_question_id_question'), 'answer', 'question', ['question_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(op.f('fk_answer_user_id_User'), 'answer', 'User', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('fk_question_user_id_user', 'question', type_='foreignkey')
    op.create_foreign_key(op.f('fk_question_user_id_User'), 'question', 'User', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_question_user_id_User'), 'question', type_='foreignkey')
    op.create_foreign_key('fk_question_user_id_user', 'question', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(op.f('fk_answer_user_id_User'), 'answer', type_='foreignkey')
    op.drop_constraint(op.f('fk_answer_question_id_question'), 'answer', type_='foreignkey')
    op.create_foreign_key('fk_answer_user_id_user', 'answer', 'user', ['user_id'], ['id'])
    op.create_foreign_key('fk_answer_question_id_question', 'answer', 'question', ['question_id'], ['id'])
    op.create_unique_constraint('uq_answer_user_id', 'answer', ['user_id'])
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('user_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('gender', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('region', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('create_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='pk_user'),
    sa.UniqueConstraint('email', name='uq_user_email'),
    sa.UniqueConstraint('username', name='uq_user_username'),
    postgresql_ignore_search_path=False
    )
    op.create_table('fridge',
    sa.Column('product_Id', sa.INTEGER(), server_default=sa.text('nextval(\'"fridge_product_Id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('product', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('barcode', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('subclass', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('qty', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('exp_date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('adding_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('modify_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('remain_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_fridge_user_id_user'),
    sa.PrimaryKeyConstraint('product_Id', name='pk_fridge'),
    sa.UniqueConstraint('product', name='uq_fridge_product')
    )
    op.create_table('barcode__categories',
    sa.Column('b_category_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('b_category_name', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('b_category_id', name='pk_barcode__categories')
    )
    op.drop_table('situation')
    op.drop_table('Recipe_situation')
    op.drop_table('Recipe_ingredient')
    op.drop_table('Fridge')
    op.drop_table('Barcode')
    op.drop_table('User')
    op.drop_table('Recipes')
    op.drop_table('Ingredient')
    op.drop_table('Barcode_companies')
    op.drop_table('Barcode_categories')
    # ### end Alembic commands ###
