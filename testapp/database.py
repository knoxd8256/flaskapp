"""Database configuration and access file.

Functions
---------
    getdb()
        This function returns a connection to the database, creating one if it does not exist.
    closedb()
        This function does exactly what it says on the tin.
    initdb()
        This function destroys all data and recreates the database.
    initapp(app)
        This function sets an application teardown job to close the database connection.
"""

# Imports

# g Object is a special Flask thing. current_app is the current app.
from flask import g
from flask import current_app

# Import configuration and sqlite modules.
import sqlite3
from testapp.config import Config


def getdb():
    """Returns a connection to the database.
    """
    if 'db' not in g:
        g.db = sqlite3.connect(
            Config.DATABASE,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def closedb(e=None):
    """Closes the conenction to the database.
    """
    db = g.pop('db', None)

    if db is not None:
        db.close()


def initdb():
    """Reinitializes and erases the database.
    """
    db = getdb()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


def initapp(app):
    """Sets a teardown function to close database connections.
    Parameters
    ---------
        app : Flask application.
            Application to set teardown function to.
    """
    app.teardown_appcontext(closedb)
