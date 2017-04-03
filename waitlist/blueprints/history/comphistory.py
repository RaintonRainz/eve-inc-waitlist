import logging
from flask.blueprints import Blueprint
from flask_login import login_required
from waitlist.permissions import perm_manager
from flask.templating import render_template

bp = Blueprint('comp_history_search', __name__)
logger = logging.getLogger(__name__)

perm_manager.define_permission('comphistory_search')


@bp.route("/", methods=['GET'])
@login_required
@perm_manager.require('comphistory_search')
def index():
    return render_template("waitlist/tools/history_search.html")
