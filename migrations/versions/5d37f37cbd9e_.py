"""empty message

Revision ID: 5d37f37cbd9e
Revises: 0bf72fa3017a
Create Date: 2023-11-18 16:05:23.742211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d37f37cbd9e'
down_revision = '0bf72fa3017a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('convidado',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('telefone', sa.String(length=11), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('convidado')
    # ### end Alembic commands ###
