"""empty message

Revision ID: 9e30d62003d0
Revises: 
Create Date: 2018-01-25 13:07:03.078775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e30d62003d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'created_at',
               existing_type=sa.DATETIME(),
               nullable=True)
    op.alter_column('tasks', 'deleted_at',
               existing_type=sa.DATETIME(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'deleted_at',
               existing_type=sa.DATETIME(),
               nullable=False)
    op.alter_column('tasks', 'created_at',
               existing_type=sa.DATETIME(),
               nullable=False)
    # ### end Alembic commands ###
