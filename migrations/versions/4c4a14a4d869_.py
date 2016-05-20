"""empty message

Revision ID: 4c4a14a4d869
Revises: 463d72677b83
Create Date: 2016-04-24 20:09:38.566000

"""

# revision identifiers, used by Alembic.
revision = '4c4a14a4d869'
down_revision = '463d72677b83'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###

    op.alter_column('comp_history', 'action',
               existing_type=mysql.VARCHAR(length=1000),
               type_=sa.String(length=20),
               existing_nullable=True)
    op.create_index(op.f('ix_comp_history_time'), 'comp_history', ['time'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comp_history_time'), table_name='comp_history')
    op.alter_column('comp_history', 'action',
               existing_type=sa.String(length=20),
               type_=mysql.VARCHAR(length=1000),
               existing_nullable=True)

    ### end Alembic commands ###