from flask.blueprints import Blueprint
import logging
from flask_login import login_required, current_user
from waitlist.data.perm import perm_management
from werkzeug.utils import redirect
from flask.globals import request, session, _app_ctx_stack
from flask_seasurf import randrange, _MAX_CSRF_KEY
import hashlib
import requests
import base64
from datetime import datetime, timedelta
from waitlist.base import db
from flask.helpers import url_for
from urllib import urlencode
from waitlist.utility.config import crest_return_url, crest_client_secret, crest_client_id
from evelink import account
from waitlist.utility.crest import create_token_cb
from pycrest.eve import AuthedConnectionB
import flask
bp = Blueprint('fc_sso', __name__)
logger = logging.getLogger(__name__)

@bp.route("/login")
@login_required
@perm_management.require(http_exception=401)
def login_redirect():
    csrf_token = get_csrf_token()
    params = urlencode({
                        'response_type': 'code',
                        'redirect_uri': crest_return_url,
                        'client_id': crest_client_id,
                        'state': 'setup-'+csrf_token,
                        'scope': 'fleetRead fleetWrite'
                        })
    return redirect("https://login.eveonline.com/oauth/authorize?"+params, code=302)

def get_sso_redirect(action):
    csrf_token = get_csrf_token()
    params = urlencode({
                        'response_type': 'code',
                        'redirect_uri': crest_return_url,
                        'client_id': crest_client_id,
                        'state': action+'-'+csrf_token,
                        'scope': 'fleetRead fleetWrite'
                        })
    return redirect("https://login.eveonline.com/oauth/authorize?"+params, code=302)

@bp.route("/cb")
@login_required
@perm_management.require(http_exception=401)
def login_cb():
    code = request.args.get('code')
    state = request.args.get('state')

    header = {'Authorization': 'Basic '+base64.b64encode(crest_client_id+":"+crest_client_secret),
              'Content-Type': 'application/x-www-form-urlencoded',
              'Host': 'login.eveonline.com'}
    params = {'grant_type': 'authorization_code',
              'code': code}
    r = requests.post("https://login.eveonline.com/oauth/token", headers=header, params=params)
    json = r.json()

    re_token = json['refresh_token']
    acc_token = json['access_token']
    exp_in = int(json['expires_in'])
    
    # lets check it matches the current character
    fleet_url = "https://crest-tq.eveonline.com/fleets/0/"
    data = {
        'access_token': acc_token,
        'refresh_token':re_token,
        'expires_in': (datetime.utcnow() + timedelta(seconds=exp_in))
        }
    connection = AuthedConnectionB(data, fleet_url, "https://login.eveonline.com/oauth", crest_client_id, crest_client_secret, create_token_cb(current_user.id))
    charName = connection.whoami()['CharacterName']
    if charName != current_user.get_eve_name():
        flask.abort(409, 'You did not grant authorization for the right character "'+current_user.get_eve_name()+'". Instead you granted it for "'+charName+'"')

    current_user.refresh_token = re_token
    current_user.access_token = acc_token
    current_user.access_token_expires = datetime.utcnow() + timedelta(seconds=exp_in)
    db.session.commit()

    if state.startswith("setup-"):
        return redirect(url_for("fleet.setup_start"))
    elif state.startswith("takeover-"):
        return redirect(url_for('fleet.takeover_sso_cb'))
    else:
        return redirect(url_for("fleet.setup_start"))
def get_csrf_token():
    csrf_name = '_csrf_token'
    csrf_token = session.get(csrf_name, None)
    if not csrf_token:
        csrf_token = generate_token()
        setattr(_app_ctx_stack.top,
                    csrf_name,
                    csrf_token)
    else:
        setattr(_app_ctx_stack.top, csrf_name, csrf_token)
    return csrf_token

def generate_token():
    salt = str(randrange(0, _MAX_CSRF_KEY)).encode('utf-8')
    return hashlib.sha1(salt).hexdigest()