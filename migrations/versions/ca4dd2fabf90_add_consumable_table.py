"""Add consumable table

Revision ID: ca4dd2fabf90
Revises: 41c9a9eb1a50
Create Date: 2021-08-30 10:23:50.202355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca4dd2fabf90'
down_revision = '41c9a9eb1a50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('consumable',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('level', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('agility', sa.Integer(), nullable=True),
    sa.Column('chance', sa.Integer(), nullable=True),
    sa.Column('intelligence', sa.Integer(), nullable=True),
    sa.Column('strength', sa.Integer(), nullable=True),
    sa.Column('wisdom', sa.Integer(), nullable=True),
    sa.Column('hp', sa.Integer(), nullable=True),
    sa.Column('energy', sa.Integer(), nullable=True),
    sa.Column('profession_bonus', sa.Integer(), nullable=True),
    sa.Column('xp_bonus', sa.Integer(), nullable=True),
    sa.Column('bonus_duration', sa.Integer(), nullable=True),
    sa.Column('conditions', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('ingredient', sa.Column('consumable_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'ingredient', 'consumable', ['consumable_id'], ['id'])
    op.add_column('recipe', sa.Column('consumable_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'recipe', 'consumable', ['consumable_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'recipe', type_='foreignkey')
    op.drop_column('recipe', 'consumable_id')
    op.drop_constraint(None, 'ingredient', type_='foreignkey')
    op.drop_column('ingredient', 'consumable_id')
    op.drop_table('consumable')
    # ### end Alembic commands ###
