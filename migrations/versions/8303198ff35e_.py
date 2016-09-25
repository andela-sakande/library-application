"""empty message

Revision ID: 8303198ff35e
Revises: 0f6c35102559
Create Date: 2016-09-25 19:10:03.773000

"""

# revision identifiers, used by Alembic.
revision = '8303198ff35e'
down_revision = '0f6c35102559'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_books_quantity', table_name='books')
    op.create_index(op.f('ix_books_quantity'), 'books', ['quantity'], unique=False)
    op.drop_index('ix_users_role', table_name='users')
    op.create_index(op.f('ix_users_role'), 'users', ['role'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_role'), table_name='users')
    op.create_index('ix_users_role', 'users', ['role'], unique=True)
    op.drop_index(op.f('ix_books_quantity'), table_name='books')
    op.create_index('ix_books_quantity', 'books', ['quantity'], unique=True)
    ### end Alembic commands ###