"""empty message

Revision ID: 5a732525f890
Revises: None
Create Date: 2018-01-24 15:13:22.638330

"""

# revision identifiers, used by Alembic.
revision = '5a732525f890'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('apicache_allianceinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('allianceName', sa.String(length=100), nullable=True),
    sa.Column('dateFounded', sa.DateTime(), nullable=True),
    sa.Column('executorCorpID', sa.Integer(), nullable=True),
    sa.Column('ticker', sa.String(length=10), nullable=True),
    sa.Column('expire', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_apicache_allianceinfo'))
    )
    op.create_index(op.f('ix_apicache_allianceinfo_allianceName'), 'apicache_allianceinfo', ['allianceName'], unique=False)
    op.create_index(op.f('ix_apicache_allianceinfo_executorCorpID'), 'apicache_allianceinfo', ['executorCorpID'], unique=False)
    op.create_table('apicache_characteraffiliation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('corporationID', sa.Integer(), nullable=True),
    sa.Column('corporationName', sa.String(length=100), nullable=True),
    sa.Column('allianceID', sa.Integer(), nullable=True),
    sa.Column('allianceName', sa.String(length=100), nullable=True),
    sa.Column('expire', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_apicache_characteraffiliation'))
    )
    op.create_index(op.f('ix_apicache_characteraffiliation_allianceID'), 'apicache_characteraffiliation', ['allianceID'], unique=False)
    op.create_index(op.f('ix_apicache_characteraffiliation_allianceName'), 'apicache_characteraffiliation', ['allianceName'], unique=False)
    op.create_index(op.f('ix_apicache_characteraffiliation_corporationID'), 'apicache_characteraffiliation', ['corporationID'], unique=False)
    op.create_index(op.f('ix_apicache_characteraffiliation_corporationName'), 'apicache_characteraffiliation', ['corporationName'], unique=False)
    op.create_index(op.f('ix_apicache_characteraffiliation_name'), 'apicache_characteraffiliation', ['name'], unique=False)
    op.create_table('apicache_characterinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('characterName', sa.String(length=100), nullable=True),
    sa.Column('corporationID', sa.Integer(), nullable=True),
    sa.Column('characterBirthday', sa.DateTime(), nullable=False),
    sa.Column('raceID', sa.Integer(), nullable=True),
    sa.Column('expire', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_apicache_characterinfo'))
    )
    op.create_index(op.f('ix_apicache_characterinfo_corporationID'), 'apicache_characterinfo', ['corporationID'], unique=False)
    op.create_table('apicache_corporationinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('allianceID', sa.Integer(), nullable=True),
    sa.Column('ceoID', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('creatorID', sa.Integer(), nullable=True),
    sa.Column('memberCount', sa.Integer(), nullable=True),
    sa.Column('taxRate', sa.Float(), nullable=True),
    sa.Column('ticker', sa.String(length=10), nullable=True),
    sa.Column('url', sa.String(length=500), nullable=True),
    sa.Column('creationDate', sa.DateTime(), nullable=True),
    sa.Column('expire', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_apicache_corporationinfo'))
    )
    op.create_index(op.f('ix_apicache_corporationinfo_allianceID'), 'apicache_corporationinfo', ['allianceID'], unique=False)
    op.create_index(op.f('ix_apicache_corporationinfo_name'), 'apicache_corporationinfo', ['name'], unique=False)
    op.create_table('calendar_category',
    sa.Column('categoryID', sa.Integer(), nullable=False),
    sa.Column('categoryName', sa.String(length=50), nullable=True),
    sa.Column('fixedTitle', sa.String(length=200), nullable=True),
    sa.Column('fixedDescription', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('categoryID', name=op.f('pk_calendar_category'))
    )
    op.create_index(op.f('ix_calendar_category_categoryName'), 'calendar_category', ['categoryName'], unique=False)
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('eve_name', sa.String(length=100), nullable=True),
    sa.Column('newbro', sa.Boolean(), nullable=False),
    sa.Column('lc_level', sa.SmallInteger(), nullable=False),
    sa.Column('cbs_level', sa.SmallInteger(), nullable=False),
    sa.Column('login_token', sa.String(length=16), nullable=True),
    sa.Column('teamspeak_poke', sa.Boolean(), server_default='1', nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_characters'))
    )
    op.create_table('constellation',
    sa.Column('constellationID', sa.Integer(), nullable=False),
    sa.Column('constellationName', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('constellationID', name=op.f('pk_constellation'))
    )
    op.create_index(op.f('ix_constellation_constellationName'), 'constellation', ['constellationName'], unique=True)
    op.create_table('eveapiscope',
    sa.Column('scopeID', sa.Integer(), nullable=False),
    sa.Column('scopeName', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('scopeID', name=op.f('pk_eveapiscope'))
    )
    op.create_index(op.f('ix_eveapiscope_scopeName'), 'eveapiscope', ['scopeName'], unique=False)
    op.create_table('event_history_types',
    sa.Column('typeID', sa.Integer(), nullable=False),
    sa.Column('typeName', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('typeID', name=op.f('pk_event_history_types')),
    sa.UniqueConstraint('typeName', name=op.f('uq_event_history_types_typeName'))
    )
    op.create_table('invmarketgroups',
    sa.Column('marketGroupID', sa.Integer(), nullable=False),
    sa.Column('parentGroupID', sa.Integer(), nullable=True),
    sa.Column('marketGroupName', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=3000), nullable=True),
    sa.Column('iconID', sa.Integer(), nullable=True),
    sa.Column('hasTypes', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['parentGroupID'], ['invmarketgroups.marketGroupID'], name=op.f('fk_invmarketgroups_parentGroupID_invmarketgroups')),
    sa.PrimaryKeyConstraint('marketGroupID', name=op.f('pk_invmarketgroups'))
    )
    op.create_table('invtypes',
    sa.Column('typeID', sa.Integer(), nullable=False),
    sa.Column('groupID', sa.Integer(), nullable=True),
    sa.Column('typeName', sa.String(length=100), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('marketGroupID', sa.BIGINT(), nullable=True),
    sa.PrimaryKeyConstraint('typeID', name=op.f('pk_invtypes'))
    )
    op.create_index('invTypes_groupid', 'invtypes', ['groupID'], unique=False)
    op.create_table('permissions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_permissions')),
    sa.UniqueConstraint('name', name=op.f('uq_permissions_name'))
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('displayName', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_roles')),
    sa.UniqueConstraint('name', name=op.f('uq_roles_name'))
    )
    op.create_table('settings',
    sa.Column('key', sa.String(length=20), nullable=False),
    sa.Column('value', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('key', name=op.f('pk_settings'))
    )
    op.create_table('solarsystem',
    sa.Column('solarSystemID', sa.Integer(), nullable=False),
    sa.Column('solarSystemName', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('solarSystemID', name=op.f('pk_solarsystem'))
    )
    op.create_index(op.f('ix_solarsystem_solarSystemName'), 'solarsystem', ['solarSystemName'], unique=True)
    op.create_table('station',
    sa.Column('stationID', sa.Integer(), nullable=False),
    sa.Column('stationName', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('stationID', name=op.f('pk_station'))
    )
    op.create_index(op.f('ix_station_stationName'), 'station', ['stationName'], unique=True)
    op.create_table('ts_dati',
    sa.Column('teamspeakID', sa.Integer(), nullable=False),
    sa.Column('displayName', sa.String(length=128), nullable=True),
    sa.Column('host', sa.String(length=128), nullable=True),
    sa.Column('port', sa.Integer(), nullable=True),
    sa.Column('displayHost', sa.String(length=128), nullable=True),
    sa.Column('displayPort', sa.Integer(), nullable=True),
    sa.Column('queryName', sa.String(length=128), nullable=True),
    sa.Column('queryPassword', sa.String(length=128), nullable=True),
    sa.Column('serverID', sa.Integer(), nullable=True),
    sa.Column('channelID', sa.Integer(), nullable=True),
    sa.Column('clientName', sa.String(length=20), nullable=True),
    sa.Column('safetyChannelID', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('teamspeakID', name=op.f('pk_ts_dati'))
    )
    op.create_table('waitlists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('groupID', sa.Integer()),
    sa.Column('displayTitle', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_waitlists'))
    )
    op.create_table('accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('current_char', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('login_token', sa.String(length=16), nullable=True),
    sa.Column('disabled', sa.Boolean(), server_default=sa.text('false'), nullable=True),
    sa.Column('had_welcome_mail', sa.Boolean(), server_default=sa.text('false'), nullable=True),
    sa.ForeignKeyConstraint(['current_char'], ['characters.id'], name=op.f('fk_accounts_current_char_characters')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_accounts')),
    sa.UniqueConstraint('login_token', name=op.f('uq_accounts_login_token')),
    sa.UniqueConstraint('username', name=op.f('uq_accounts_username'))
    )
    op.create_table('ban',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('reason', sa.Text(), nullable=True),
    sa.Column('admin', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['admin'], ['characters.id'], name=op.f('fk_ban_admin_characters')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_ban'))
    )
    op.create_index(op.f('ix_ban_name'), 'ban', ['name'], unique=False)
    op.create_table('event_history_entries',
    sa.Column('historyID', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('typeID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['typeID'], ['event_history_types.typeID'], name=op.f('fk_event_history_entries_typeID_event_history_types')),
    sa.PrimaryKeyConstraint('historyID', name=op.f('pk_event_history_entries'))
    )
    op.create_index(op.f('ix_event_history_entries_time'), 'event_history_entries', ['time'], unique=False)
    op.create_table('feedback',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('last_changed', sa.DateTime(), nullable=True),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.Column('likes', sa.Boolean(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['characters.id'], name=op.f('fk_feedback_user_characters')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_feedback'))
    )
    op.create_index(op.f('ix_feedback_last_changed'), 'feedback', ['last_changed'], unique=False)
    op.create_index(op.f('ix_feedback_user'), 'feedback', ['user'], unique=True)
    op.create_table('fittings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ship_type', sa.Integer(), nullable=True),
    sa.Column('modules', sa.String(length=5000), nullable=True),
    sa.Column('comment', sa.String(length=5000), nullable=True),
    sa.Column('wl_type', sa.String(length=10), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['ship_type'], ['invtypes.typeID'], name=op.f('fk_fittings_ship_type_invtypes')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_fittings'))
    )
    op.create_table('incursion_layout',
    sa.Column('constellation', sa.Integer(), nullable=False),
    sa.Column('staging', sa.Integer(), nullable=True),
    sa.Column('headquarter', sa.Integer(), nullable=True),
    sa.Column('dockup', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['constellation'], ['constellation.constellationID'], name=op.f('fk_incursion_layout_constellation_constellation')),
    sa.ForeignKeyConstraint(['dockup'], ['station.stationID'], name=op.f('fk_incursion_layout_dockup_station')),
    sa.ForeignKeyConstraint(['headquarter'], ['solarsystem.solarSystemID'], name=op.f('fk_incursion_layout_headquarter_solarsystem')),
    sa.ForeignKeyConstraint(['staging'], ['solarsystem.solarSystemID'], name=op.f('fk_incursion_layout_staging_solarsystem')),
    sa.PrimaryKeyConstraint('constellation', name=op.f('pk_incursion_layout'))
    )
    op.create_table('permission_roles',
    sa.Column('permission', sa.Integer(), nullable=True),
    sa.Column('role', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['permission'], ['permissions.id'], name=op.f('fk_permission_roles_permission_permissions')),
    sa.ForeignKeyConstraint(['role'], ['roles.id'], name=op.f('fk_permission_roles_role_roles'))
    )
    op.create_table('tickets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('characterID', sa.Integer(), nullable=True),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('state', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['characterID'], ['characters.id'], name=op.f('fk_tickets_characterID_characters')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_tickets'))
    )
    op.create_index(op.f('ix_tickets_characterID'), 'tickets', ['characterID'], unique=False)
    op.create_index(op.f('ix_tickets_state'), 'tickets', ['state'], unique=False)
    op.create_index(op.f('ix_tickets_time'), 'tickets', ['time'], unique=False)
    op.create_table('waitlist_entries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('creation', sa.DateTime(), nullable=True),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.Column('waitlist_id', sa.Integer(), nullable=True),
    sa.Column('timeInvited', sa.DateTime(), nullable=True),
    sa.Column('inviteCount', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['characters.id'], name=op.f('fk_waitlist_entries_user_characters')),
    sa.ForeignKeyConstraint(['waitlist_id'], ['waitlists.id'], name=op.f('fk_waitlist_entries_waitlist_id_waitlists'), onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_waitlist_entries'))
    )
    op.create_table('waitlist_groups',
    sa.Column('groupID', sa.Integer(), nullable=False),
    sa.Column('groupName', sa.String(length=50), nullable=False),
    sa.Column('displayName', sa.String(length=50), nullable=False),
    sa.Column('xupwlID', sa.Integer(), nullable=False),
    sa.Column('logiwlID', sa.Integer(), nullable=False),
    sa.Column('dpswlID', sa.Integer(), nullable=False),
    sa.Column('sniperwlID', sa.Integer(), nullable=False),
    sa.Column('otherwlID', sa.Integer(), nullable=True),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.Column('status', sa.String(length=1000), nullable=True),
    sa.Column('dockupID', sa.Integer(), nullable=True),
    sa.Column('systemID', sa.Integer(), nullable=True),
    sa.Column('constellationID', sa.Integer(), nullable=True),
    sa.Column('odering', sa.Integer(), nullable=False),
    sa.Column('influence', sa.Boolean(), server_default='0', nullable=False),
    sa.ForeignKeyConstraint(['constellationID'], ['constellation.constellationID'], name=op.f('fk_waitlist_groups_constellationID_constellation')),
    sa.ForeignKeyConstraint(['dockupID'], ['station.stationID'], name=op.f('fk_waitlist_groups_dockupID_station')),
    sa.ForeignKeyConstraint(['dpswlID'], ['waitlists.id'], name=op.f('fk_waitlist_groups_dpswlID_waitlists')),
    sa.ForeignKeyConstraint(['logiwlID'], ['waitlists.id'], name=op.f('fk_waitlist_groups_logiwlID_waitlists')),
    sa.ForeignKeyConstraint(['otherwlID'], ['waitlists.id'], name=op.f('fk_waitlist_groups_otherwlID_waitlists')),
    sa.ForeignKeyConstraint(['sniperwlID'], ['waitlists.id'], name=op.f('fk_waitlist_groups_sniperwlID_waitlists')),
    sa.ForeignKeyConstraint(['systemID'], ['solarsystem.solarSystemID'], name=op.f('fk_waitlist_groups_systemID_solarsystem')),
    sa.ForeignKeyConstraint(['xupwlID'], ['waitlists.id'], name=op.f('fk_waitlist_groups_xupwlID_waitlists')),
    sa.PrimaryKeyConstraint('groupID', name=op.f('pk_waitlist_groups')),
    sa.UniqueConstraint('displayName', name=op.f('uq_waitlist_groups_displayName')),
    sa.UniqueConstraint('groupName', name=op.f('uq_waitlist_groups_groupName'))
    )
    op.create_table('whitelist',
    sa.Column('characterID', sa.Integer(), nullable=False),
    sa.Column('reason', sa.Text(), nullable=True),
    sa.Column('adminID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['adminID'], ['characters.id'], name=op.f('fk_whitelist_adminID_characters')),
    sa.ForeignKeyConstraint(['characterID'], ['characters.id'], name=op.f('fk_whitelist_characterID_characters')),
    sa.PrimaryKeyConstraint('characterID', name=op.f('pk_whitelist'))
    )
    op.create_table('account_notes',
    sa.Column('entryID', sa.Integer(), nullable=False),
    sa.Column('accountID', sa.Integer(), nullable=False),
    sa.Column('byAccountID', sa.Integer(), nullable=False),
    sa.Column('note', sa.Text(), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('restriction_level', sa.SmallInteger(), server_default=sa.text('50'), nullable=False),
    sa.ForeignKeyConstraint(['accountID'], ['accounts.id'], name=op.f('fk_account_notes_accountID_accounts')),
    sa.ForeignKeyConstraint(['byAccountID'], ['accounts.id'], name=op.f('fk_account_notes_byAccountID_accounts')),
    sa.PrimaryKeyConstraint('entryID', name=op.f('pk_account_notes'))
    )
    op.create_index(op.f('ix_account_notes_time'), 'account_notes', ['time'], unique=False)
    op.create_table('account_roles',
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['accounts.id'], name=op.f('fk_account_roles_account_id_accounts'), onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], name=op.f('fk_account_roles_role_id_roles'), onupdate='CASCADE', ondelete='CASCADE')
    )
    op.create_table('backseats',
    sa.Column('accountID', sa.Integer(), nullable=True),
    sa.Column('groupID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['accountID'], ['accounts.id'], name=op.f('fk_backseats_accountID_accounts'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['groupID'], ['waitlist_groups.groupID'], name=op.f('fk_backseats_groupID_waitlist_groups'), ondelete='CASCADE')
    )
    op.create_table('calendar_event',
    sa.Column('eventID', sa.Integer(), nullable=False),
    sa.Column('eventCreatorID', sa.Integer(), nullable=True),
    sa.Column('eventTitle', sa.Text(), nullable=True),
    sa.Column('eventDescription', sa.Text(), nullable=True),
    sa.Column('eventCategoryID', sa.Integer(), nullable=True),
    sa.Column('eventApproved', sa.Boolean(), nullable=True),
    sa.Column('eventTime', sa.DateTime(), nullable=True),
    sa.Column('approverID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['approverID'], ['accounts.id'], name=op.f('fk_calendar_event_approverID_accounts'), onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['eventCategoryID'], ['calendar_category.categoryID'], name=op.f('fk_calendar_event_eventCategoryID_calendar_category'), onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['eventCreatorID'], ['accounts.id'], name=op.f('fk_calendar_event_eventCreatorID_accounts'), onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('eventID', name=op.f('pk_calendar_event'))
    )
    op.create_index(op.f('ix_calendar_event_eventApproved'), 'calendar_event', ['eventApproved'], unique=False)
    op.create_index(op.f('ix_calendar_event_eventCategoryID'), 'calendar_event', ['eventCategoryID'], unique=False)
    op.create_index(op.f('ix_calendar_event_eventCreatorID'), 'calendar_event', ['eventCreatorID'], unique=False)
    op.create_index(op.f('ix_calendar_event_eventTime'), 'calendar_event', ['eventTime'], unique=False)
    op.create_table('ccvote',
    sa.Column('ccvoteID', sa.Integer(), nullable=False),
    sa.Column('voterID', sa.Integer(), nullable=True),
    sa.Column('lmvoteID', sa.Integer(), nullable=True),
    sa.Column('fcvoteID', sa.Integer(), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['fcvoteID'], ['accounts.id'], name=op.f('fk_ccvote_fcvoteID_accounts')),
    sa.ForeignKeyConstraint(['lmvoteID'], ['accounts.id'], name=op.f('fk_ccvote_lmvoteID_accounts')),
    sa.ForeignKeyConstraint(['voterID'], ['characters.id'], name=op.f('fk_ccvote_voterID_characters')),
    sa.PrimaryKeyConstraint('ccvoteID', name=op.f('pk_ccvote'))
    )
    op.create_table('comp_history',
    sa.Column('historyID', sa.Integer(), nullable=False),
    sa.Column('sourceID', sa.Integer(), nullable=True),
    sa.Column('targetID', sa.Integer(), nullable=False),
    sa.Column('action', sa.String(length=20), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('exref', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sourceID'], ['accounts.id'], name=op.f('fk_comp_history_sourceID_accounts')),
    sa.ForeignKeyConstraint(['targetID'], ['characters.id'], name=op.f('fk_comp_history_targetID_characters')),
    sa.PrimaryKeyConstraint('historyID', name=op.f('pk_comp_history'))
    )
    op.create_index(op.f('ix_comp_history_time'), 'comp_history', ['time'], unique=False)
    op.create_table('crest_fleets',
    sa.Column('fleetID', sa.BigInteger(), nullable=False),
    sa.Column('logiWingID', sa.BigInteger(), nullable=True),
    sa.Column('logiSquadID', sa.BigInteger(), nullable=True),
    sa.Column('sniperWingID', sa.BigInteger(), nullable=True),
    sa.Column('sniperSquadID', sa.BigInteger(), nullable=True),
    sa.Column('dpsWingID', sa.BigInteger(), nullable=True),
    sa.Column('dpsSquadID', sa.BigInteger(), nullable=True),
    sa.Column('otherWingID', sa.BigInteger(), nullable=True),
    sa.Column('otherSquadID', sa.BigInteger(), nullable=True),
    sa.Column('groupID', sa.Integer(), nullable=False),
    sa.Column('compID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['compID'], ['accounts.id'], name=op.f('fk_crest_fleets_compID_accounts')),
    sa.ForeignKeyConstraint(['groupID'], ['waitlist_groups.groupID'], name=op.f('fk_crest_fleets_groupID_waitlist_groups')),
    sa.PrimaryKeyConstraint('fleetID', name=op.f('pk_crest_fleets'))
    )
    op.create_table('event_history_info',
    sa.Column('infoID', sa.Integer(), nullable=False),
    sa.Column('historyID', sa.Integer(), nullable=True),
    sa.Column('infoType', sa.Integer(), nullable=True),
    sa.Column('referenceID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['historyID'], ['event_history_entries.historyID'], name=op.f('fk_event_history_info_historyID_event_history_entries')),
    sa.PrimaryKeyConstraint('infoID', name=op.f('pk_event_history_info'))
    )
    op.create_table('fcs',
    sa.Column('accountID', sa.Integer(), nullable=True),
    sa.Column('groupID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['accountID'], ['accounts.id'], name=op.f('fk_fcs_accountID_accounts'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['groupID'], ['waitlist_groups.groupID'], name=op.f('fk_fcs_groupID_waitlist_groups'), ondelete='CASCADE')
    )
    op.create_table('fit_module',
    sa.Column('fitID', sa.Integer(), nullable=False),
    sa.Column('moduleID', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fitID'], ['fittings.id'], name=op.f('fk_fit_module_fitID_fittings')),
    sa.ForeignKeyConstraint(['moduleID'], ['invtypes.typeID'], name=op.f('fk_fit_module_moduleID_invtypes')),
    sa.PrimaryKeyConstraint('fitID', 'moduleID', name=op.f('pk_fit_module'))
    )
    op.create_table('fleetmanager',
    sa.Column('accountID', sa.Integer(), nullable=True),
    sa.Column('groupID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['accountID'], ['accounts.id'], name=op.f('fk_fleetmanager_accountID_accounts'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['groupID'], ['waitlist_groups.groupID'], name=op.f('fk_fleetmanager_groupID_waitlist_groups'), ondelete='CASCADE')
    )
    op.create_table('linked_chars',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('char_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['char_id'], ['characters.id'], name=op.f('fk_linked_chars_char_id_characters'), onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id'], ['accounts.id'], name=op.f('fk_linked_chars_id_accounts'), onupdate='CASCADE', ondelete='CASCADE')
    )
    op.create_table('ssotoken',
    sa.Column('accountID', sa.Integer(), nullable=False),
    sa.Column('refresh_token', sa.String(length=128), nullable=True),
    sa.Column('access_token', sa.String(length=128), nullable=True),
    sa.Column('access_token_expires', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['accountID'], ['accounts.id'], name=op.f('fk_ssotoken_accountID_accounts'), onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('accountID', name=op.f('pk_ssotoken'))
    )
    op.create_table('trivia',
    sa.Column('triviaID', sa.Integer(), nullable=False),
    sa.Column('createdByID', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=5000), nullable=True),
    sa.Column('alertText', sa.String(length=1000), nullable=True),
    sa.Column('fromTime', sa.DateTime(), nullable=True),
    sa.Column('toTime', sa.DateTime(), nullable=True),
    sa.CheckConstraint('"toTime" > "fromTime"', name=op.f('ck_trivia_to_biggerthen_from')),
    sa.ForeignKeyConstraint(['createdByID'], ['accounts.id'], name=op.f('fk_trivia_createdByID_accounts')),
    sa.PrimaryKeyConstraint('triviaID', name=op.f('pk_trivia'))
    )
    op.create_table('waitlist_entry_fits',
    sa.Column('entryID', sa.Integer(), nullable=True),
    sa.Column('fitID', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['entryID'], ['waitlist_entries.id'], name=op.f('fk_waitlist_entry_fits_entryID_waitlist_entries'), onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['fitID'], ['fittings.id'], name=op.f('fk_waitlist_entry_fits_fitID_fittings'), onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('fitID', name=op.f('pk_waitlist_entry_fits'))
    )
    op.create_table('calendar_backseat',
    sa.Column('accountID', sa.Integer(), nullable=True),
    sa.Column('eventID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['accountID'], ['accounts.id'], name=op.f('fk_calendar_backseat_accountID_accounts'), onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['eventID'], ['calendar_event.eventID'], name=op.f('fk_calendar_backseat_eventID_calendar_event'), onupdate='CASCADE', ondelete='CASCADE')
    )
    op.create_table('calendar_organizer',
    sa.Column('accountID', sa.Integer(), nullable=True),
    sa.Column('eventID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['accountID'], ['accounts.id'], name=op.f('fk_calendar_organizer_accountID_accounts'), onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['eventID'], ['calendar_event.eventID'], name=op.f('fk_calendar_organizer_eventID_calendar_event'), onupdate='CASCADE', ondelete='CASCADE')
    )
    op.create_table('comp_history_ext_inv',
    sa.Column('inviteExtID', sa.Integer(), nullable=False),
    sa.Column('historyID', sa.Integer(), nullable=True),
    sa.Column('waitlistID', sa.Integer(), nullable=True),
    sa.Column('timeCreated', sa.DateTime(), nullable=True),
    sa.Column('timeInvited', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['historyID'], ['comp_history.historyID'], name=op.f('fk_comp_history_ext_inv_historyID_comp_history')),
    sa.ForeignKeyConstraint(['waitlistID'], ['waitlists.id'], name=op.f('fk_comp_history_ext_inv_waitlistID_waitlists')),
    sa.PrimaryKeyConstraint('inviteExtID', name=op.f('pk_comp_history_ext_inv'))
    )
    op.create_table('comp_history_fits',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('historyID', sa.Integer(), nullable=True),
    sa.Column('fitID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fitID'], ['fittings.id'], name=op.f('fk_comp_history_fits_fitID_fittings')),
    sa.ForeignKeyConstraint(['historyID'], ['comp_history.historyID'], name=op.f('fk_comp_history_fits_historyID_comp_history')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_comp_history_fits'))
    )
    op.create_table('role_changes',
    sa.Column('roleChangeID', sa.Integer(), nullable=False),
    sa.Column('entryID', sa.Integer(), nullable=False),
    sa.Column('roleID', sa.Integer(), nullable=False),
    sa.Column('added', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['entryID'], ['account_notes.entryID'], name=op.f('fk_role_changes_entryID_account_notes'), onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['roleID'], ['roles.id'], name=op.f('fk_role_changes_roleID_roles'), onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('roleChangeID', name=op.f('pk_role_changes'))
    )
    op.create_table('tokenscope',
    sa.Column('tokenID', sa.Integer(), nullable=False),
    sa.Column('scopeID', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['scopeID'], ['eveapiscope.scopeID'], name=op.f('fk_tokenscope_scopeID_eveapiscope'), onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['tokenID'], ['ssotoken.accountID'], name=op.f('fk_tokenscope_tokenID_ssotoken'), onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('tokenID', 'scopeID', name=op.f('pk_tokenscope'))
    )
    op.create_table('trivia_question',
    sa.Column('questionID', sa.Integer(), nullable=False),
    sa.Column('triviaID', sa.Integer(), nullable=True),
    sa.Column('questionText', sa.String(length=1000), nullable=True),
    sa.Column('answerType', sa.String(length=255), nullable=True),
    sa.Column('answerConnection', sa.Enum('AND', 'OR', 'NOT', 'NONE', name='answer_connection_type'), nullable=True),
    sa.Column('inputPlaceholder', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['triviaID'], ['trivia.triviaID'], name=op.f('fk_trivia_question_triviaID_trivia')),
    sa.PrimaryKeyConstraint('questionID', name=op.f('pk_trivia_question'))
    )
    op.create_table('trivia_submission',
    sa.Column('submissionID', sa.Integer(), nullable=False),
    sa.Column('triviaID', sa.Integer(), nullable=True),
    sa.Column('submittorID', sa.Integer(), nullable=True),
    sa.Column('submittorAccountID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['submittorAccountID'], ['accounts.id'], name=op.f('fk_trivia_submission_submittorAccountID_accounts')),
    sa.ForeignKeyConstraint(['submittorID'], ['characters.id'], name=op.f('fk_trivia_submission_submittorID_characters')),
    sa.ForeignKeyConstraint(['triviaID'], ['trivia.triviaID'], name=op.f('fk_trivia_submission_triviaID_trivia')),
    sa.PrimaryKeyConstraint('submissionID', name=op.f('pk_trivia_submission'))
    )
    op.create_table('trivia_answer',
    sa.Column('answerID', sa.Integer(), nullable=False),
    sa.Column('questionID', sa.Integer(), nullable=False),
    sa.Column('answerText', sa.String(length=1000), nullable=True),
    sa.ForeignKeyConstraint(['questionID'], ['trivia_question.questionID'], name=op.f('fk_trivia_answer_questionID_trivia_question')),
    sa.PrimaryKeyConstraint('answerID', 'questionID', name=op.f('pk_trivia_answer'))
    )
    op.create_table('trivia_submission_answer',
    sa.Column('submissionID', sa.Integer(), nullable=False),
    sa.Column('questionID', sa.Integer(), nullable=False),
    sa.Column('answerText', sa.String(length=5000), nullable=True),
    sa.ForeignKeyConstraint(['questionID'], ['trivia_question.questionID'], name=op.f('fk_trivia_submission_answer_questionID_trivia_question')),
    sa.ForeignKeyConstraint(['submissionID'], ['trivia_submission.submissionID'], name=op.f('fk_trivia_submission_answer_submissionID_trivia_submission')),
    sa.PrimaryKeyConstraint('submissionID', 'questionID', name=op.f('pk_trivia_submission_answer'))
    )

    op.create_foreign_key("fk_waitlists_groupID_waitlist_groups", "waitlists", "waitlist_groups", ["groupID"], ["groupID"])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trivia_submission_answer')
    op.drop_table('trivia_answer')
    op.drop_table('trivia_submission')
    op.drop_table('trivia_question')
    op.drop_table('tokenscope')
    op.drop_table('role_changes')
    op.drop_table('comp_history_fits')
    op.drop_table('comp_history_ext_inv')
    op.drop_table('calendar_organizer')
    op.drop_table('calendar_backseat')
    op.drop_table('waitlist_entry_fits')
    op.drop_table('trivia')
    op.drop_table('ssotoken')
    op.drop_table('linked_chars')
    op.drop_table('fleetmanager')
    op.drop_table('fit_module')
    op.drop_table('fcs')
    op.drop_table('event_history_info')
    op.drop_table('crest_fleets')
    op.drop_index(op.f('ix_comp_history_time'), table_name='comp_history')
    op.drop_table('comp_history')
    op.drop_table('ccvote')
    op.drop_index(op.f('ix_calendar_event_eventTime'), table_name='calendar_event')
    op.drop_index(op.f('ix_calendar_event_eventCreatorID'), table_name='calendar_event')
    op.drop_index(op.f('ix_calendar_event_eventCategoryID'), table_name='calendar_event')
    op.drop_index(op.f('ix_calendar_event_eventApproved'), table_name='calendar_event')
    op.drop_table('calendar_event')
    op.drop_table('backseats')
    op.drop_table('account_roles')
    op.drop_index(op.f('ix_account_notes_time'), table_name='account_notes')
    op.drop_table('account_notes')
    op.drop_table('whitelist')
    op.drop_table('waitlist_groups')
    op.drop_table('waitlist_entries')
    op.drop_index(op.f('ix_tickets_time'), table_name='tickets')
    op.drop_index(op.f('ix_tickets_state'), table_name='tickets')
    op.drop_index(op.f('ix_tickets_characterID'), table_name='tickets')
    op.drop_table('tickets')
    op.drop_table('permission_roles')
    op.drop_table('incursion_layout')
    op.drop_table('fittings')
    op.drop_index(op.f('ix_feedback_user'), table_name='feedback')
    op.drop_index(op.f('ix_feedback_last_changed'), table_name='feedback')
    op.drop_table('feedback')
    op.drop_index(op.f('ix_event_history_entries_time'), table_name='event_history_entries')
    op.drop_table('event_history_entries')
    op.drop_index(op.f('ix_ban_name'), table_name='ban')
    op.drop_table('ban')
    op.drop_table('accounts')
    op.drop_table('waitlists')
    op.drop_table('ts_dati')
    op.drop_index(op.f('ix_station_stationName'), table_name='station')
    op.drop_table('station')
    op.drop_index(op.f('ix_solarsystem_solarSystemName'), table_name='solarsystem')
    op.drop_table('solarsystem')
    op.drop_table('settings')
    op.drop_table('roles')
    op.drop_table('permissions')
    op.drop_index('invTypes_groupid', table_name='invtypes')
    op.drop_table('invtypes')
    op.drop_table('invmarketgroups')
    op.drop_table('event_history_types')
    op.drop_index(op.f('ix_eveapiscope_scopeName'), table_name='eveapiscope')
    op.drop_table('eveapiscope')
    op.drop_index(op.f('ix_constellation_constellationName'), table_name='constellation')
    op.drop_table('constellation')
    op.drop_table('characters')
    op.drop_index(op.f('ix_calendar_category_categoryName'), table_name='calendar_category')
    op.drop_table('calendar_category')
    op.drop_index(op.f('ix_apicache_corporationinfo_name'), table_name='apicache_corporationinfo')
    op.drop_index(op.f('ix_apicache_corporationinfo_allianceID'), table_name='apicache_corporationinfo')
    op.drop_table('apicache_corporationinfo')
    op.drop_index(op.f('ix_apicache_characterinfo_corporationID'), table_name='apicache_characterinfo')
    op.drop_table('apicache_characterinfo')
    op.drop_index(op.f('ix_apicache_characteraffiliation_name'), table_name='apicache_characteraffiliation')
    op.drop_index(op.f('ix_apicache_characteraffiliation_corporationName'), table_name='apicache_characteraffiliation')
    op.drop_index(op.f('ix_apicache_characteraffiliation_corporationID'), table_name='apicache_characteraffiliation')
    op.drop_index(op.f('ix_apicache_characteraffiliation_allianceName'), table_name='apicache_characteraffiliation')
    op.drop_index(op.f('ix_apicache_characteraffiliation_allianceID'), table_name='apicache_characteraffiliation')
    op.drop_table('apicache_characteraffiliation')
    op.drop_index(op.f('ix_apicache_allianceinfo_executorCorpID'), table_name='apicache_allianceinfo')
    op.drop_index(op.f('ix_apicache_allianceinfo_allianceName'), table_name='apicache_allianceinfo')
    op.drop_table('apicache_allianceinfo')
    # ### end Alembic commands ###
