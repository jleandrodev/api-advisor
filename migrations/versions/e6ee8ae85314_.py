"""empty message

Revision ID: e6ee8ae85314
Revises: 4f481e3fc44f
Create Date: 2023-11-26 13:47:18.014240

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e6ee8ae85314'
down_revision = '4f481e3fc44f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('acompanhante', schema=None) as batch_op:
        batch_op.alter_column('idade',
               existing_type=mysql.VARCHAR(length=12),
               type_=sa.Enum('ZERO_CINCO_ANOS', 'SEIS_DEZ_ANOS', 'ADULTO', name='faixaetaria'),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('acompanhante', schema=None) as batch_op:
        batch_op.alter_column('idade',
               existing_type=sa.Enum('ZERO_CINCO_ANOS', 'SEIS_DEZ_ANOS', 'ADULTO', name='faixaetaria'),
               type_=mysql.VARCHAR(length=12),
               existing_nullable=False)

    # ### end Alembic commands ###
