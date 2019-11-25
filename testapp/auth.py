"""Authorization page blueprint.
"""
import functools

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from testapp.database import getdb

# Registering blueprint to be used by the application.
bp = Blueprint('auth', __name__, url_prefix='/auth')


# Registration page route.
@bp.route('/register', methods=('GET', 'POST'))
def register():
    """Registration form route.

    Returns
    -------
    HTML page.
        Registration form, or results thereof.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = getdb()
        error = None

        if not username:
            error = 'Please enter a username.'
        elif not password:
            error = 'Please enter a password.'
        elif db.execute('SELECT id FROM flaskuser WHERE username = ?', (username, )).fetchone() is not None:
            error = 'Username is taken. Enter another!'

        if error is None:
            db.execute(
                'INSERT INTO flaskuser (username, pword) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))
        flash(error)
    return render_template('auth/register.html', title="Register")


# Login page route.
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = getdb()
        error = None
        user = db.execute(
            'SELECT * FROM flaskuser WHERE username = ?', (username,)
        ).fetchone()

        if user is None or not check_password_hash(user['pword'], password):
            error = 'Username or password is incorrect.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html', title='Login')


# Logout route.
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


# User loader from session.
@bp.before_app_request
def load_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = getdb().execute(
            'SELECT * FROM flaskuser WHERE id = ?', (user_id,)
        ).fetchone()


# Login requirement decorator.
def login_required(view):
    @functools.wraps(view)
    def view_wrapper(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        else:
            return view(**kwargs)
    return view_wrapper
