"""empty message

Revision ID: 272c63e29481
Revises: d55b515fdfb5
Create Date: 2023-11-18 21:41:34.092833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '272c63e29481'
down_revision = 'd55b515fdfb5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assistente',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('telefone', sa.String(length=11), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('assistente')
    # ### end Alembic commands ###
