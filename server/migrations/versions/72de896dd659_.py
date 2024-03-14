"""empty message

Revision ID: 72de896dd659
Revises: 6790a37f225b
Create Date: 2024-03-13 19:27:06.445690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72de896dd659'
down_revision = '6790a37f225b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('body', sa.String(), nullable=True))
    op.add_column('messages', sa.Column('username', sa.String(), nullable=True))
    op.add_column('messages', sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
    op.add_column('messages', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'updated_at')
    op.drop_column('messages', 'created_at')
    op.drop_column('messages', 'username')
    op.drop_column('messages', 'body')
    # ### end Alembic commands ###
