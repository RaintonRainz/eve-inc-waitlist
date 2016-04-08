"""empty message

Revision ID: 913428ec59ed
Revises: f3b1988db9b9
Create Date: 2016-04-07 23:09:03.497000

"""

# revision identifiers, used by Alembic.
revision = '913428ec59ed'
down_revision = 'f3b1988db9b9'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('waitlist_entry_fits', 'id')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('waitlist_entry_fits', sa.Column('id', mysql.INTEGER(display_width=11), nullable=False))
    ### end Alembic commands ###
