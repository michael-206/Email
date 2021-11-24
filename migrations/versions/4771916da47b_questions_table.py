"""questions table

Revision ID: 4771916da47b
Revises: 7bc89589e9cd
Create Date: 2021-11-23 19:35:20.342981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4771916da47b'
down_revision = '7bc89589e9cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Documents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('body', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.Text(), nullable=False),
    sa.Column('answer', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Questions')
    op.drop_table('Documents')
    # ### end Alembic commands ###
