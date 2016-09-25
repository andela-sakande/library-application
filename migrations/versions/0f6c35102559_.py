"""empty message

Revision ID: 0f6c35102559
Revises: None
Create Date: 2016-09-25 18:58:37.504000

"""

# revision identifiers, used by Alembic.
revision = '0f6c35102559'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_categories_name'), 'categories', ['name'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=64), nullable=True),
    sa.Column('lastname', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('pwdhash', sa.String(length=128), nullable=True),
    sa.Column('role', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_firstname'), 'users', ['firstname'], unique=False)
    op.create_index(op.f('ix_users_lastname'), 'users', ['lastname'], unique=False)
    op.create_index(op.f('ix_users_pwdhash'), 'users', ['pwdhash'], unique=False)
    op.create_index(op.f('ix_users_role'), 'users', ['role'], unique=True)
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=True),
    sa.Column('author', sa.String(length=120), nullable=True),
    sa.Column('isbn', sa.String(length=60), nullable=True),
    sa.Column('categoryid', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['categoryid'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_books_author'), 'books', ['author'], unique=False)
    op.create_index(op.f('ix_books_isbn'), 'books', ['isbn'], unique=True)
    op.create_index(op.f('ix_books_quantity'), 'books', ['quantity'], unique=True)
    op.create_index(op.f('ix_books_title'), 'books', ['title'], unique=True)
    op.create_table('borrowedbooks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bookid', sa.Integer(), nullable=True),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('timeborrowed', sa.DateTime(), nullable=True),
    sa.Column('timereturned', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['bookid'], ['books.id'], ),
    sa.ForeignKeyConstraint(['userid'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('borrowedbooks')
    op.drop_index(op.f('ix_books_title'), table_name='books')
    op.drop_index(op.f('ix_books_quantity'), table_name='books')
    op.drop_index(op.f('ix_books_isbn'), table_name='books')
    op.drop_index(op.f('ix_books_author'), table_name='books')
    op.drop_table('books')
    op.drop_index(op.f('ix_users_role'), table_name='users')
    op.drop_index(op.f('ix_users_pwdhash'), table_name='users')
    op.drop_index(op.f('ix_users_lastname'), table_name='users')
    op.drop_index(op.f('ix_users_firstname'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_categories_name'), table_name='categories')
    op.drop_table('categories')
    ### end Alembic commands ###
