"""empty message

Revision ID: 11ee20a79069
Revises: 4f84a51ec263
Create Date: 2016-04-07 22:43:19.593000

"""

# revision identifiers, used by Alembic.
revision = '11ee20a79069'
down_revision = '4f84a51ec263'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'fittings_ibfk_2', 'fittings', type_='foreignkey')
    op.create_foreign_key('fittings_ibfk_2', 'fittings', 'waitlist_entries', ['waitlist_id'], ['id'], onupdate='CASCADE')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fittings_ibfk_2', 'fittings', type_='foreignkey')
    op.create_foreign_key(u'fittings_ibfk_2', 'fittings', 'waitlist_entries', ['waitlist_id'], ['id'], onupdate=u'CASCADE', ondelete=u'CASCADE')
    ### end Alembic commands ###
