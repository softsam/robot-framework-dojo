import base64
import logging
from login import UserDataBase
from flask import Flask, request, redirect, url_for, render_template, make_response, session
from functools import wraps

opened_database = None
logging.basicConfig(level=logging.DEBUG, format='%(message)s')
logger = logging.getLogger(__name__)


def check_auth(username, password):
    global opened_database
    return opened_database.check_credentials(username, password) == UserDataBase.SUCCESS


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return _render_login(error='Unauthorized')


def requires_auth(f):
    global logger

    @wraps(f)
    def decorated(*args, **kwargs):
        if 'Authorization' not in session:
            logger.debug('not authenticated')
            return authenticate()
        else:
            logger.debug('authenticated: %s' % base64.b64decode(session['Authorization'])[6:])
            return f(*args, **kwargs)

    return decorated


def _render_login(error=None):
    return render_template('signin.html', error=error)


def _redirect_home_with_credentials(username, password):
    global logger
    logger.debug('setting credentials and rendering login')
    session['Authorization'] = base64.b64encode('Basic %s:%s' % (username, password))
    return redirect(url_for('home'))


app = Flask(__name__)
app.secret_key = 'No secret is well kept'


@app.route("/", methods=['GET'])
@requires_auth
def home():
    logger.debug('home')
    return render_template('home.html')


@app.route("/signin", methods=['GET', 'POST'])
def signin():
    logger.debug('signin')
    if request.method == 'GET':
        return _render_login()
    else:  # a POST because others are not allowed
        username = request.form['username']
        password = request.form['password']
        if not check_auth(username, password):
            return _render_login(error='Invalid credentials')
        else:
            return _redirect_home_with_credentials(username, password)


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    logger.debug('signup')
    global opened_database
    if request.method == 'GET':
        return render_template('signup.html')
    else:  # a POST because others are not allowed
        username = request.form['username']
        password = request.form['password']
        create_status = opened_database.create_user(username, password)
        if create_status == UserDataBase.SUCCESS:
            return _redirect_home_with_credentials(username, password)
        else:
            return render_template('signup.html', error=create_status)


@app.route("/signout", methods=['GET', 'POST'])
def signout():
    logger.debug('signout')
    if 'Authorization' in session:
        session.pop('Authorization')
    return _render_login(error='Logged out')


if __name__ == "__main__":
    with UserDataBase() as db:
        opened_database = db
        app.run()
