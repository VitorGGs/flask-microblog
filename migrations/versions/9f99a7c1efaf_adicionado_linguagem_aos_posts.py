"""adicionado linguagem aos posts

Revision ID: 9f99a7c1efaf
Revises: 90a6398b0bca
Create Date: 2020-09-21 14:54:48.945833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f99a7c1efaf'
down_revision = '90a6398b0bca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
