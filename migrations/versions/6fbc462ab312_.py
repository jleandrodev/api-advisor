"""empty message

Revision ID: 6fbc462ab312
Revises: b4e21cd36c96
Create Date: 2023-11-26 12:12:40.469260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fbc462ab312'
down_revision = 'b4e21cd36c96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('acompanhante',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('idade', sa.Enum('ZERO_CINCO_ANOS', 'SEIS_DEZ_ANOS', 'ADULTO', name='faixaetaria'), nullable=False),
    sa.Column('convidado_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['convidado_id'], ['convidado.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('acompanhante')
    # ### end Alembic commands ###
