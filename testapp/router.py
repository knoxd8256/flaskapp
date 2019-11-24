"""
This file contains router functions for flask to access from test.py.

Functions
---------
    index
        This is the route for '/' and '/index'
"""
# Importing template rendering engine.
from flask import render_template


# Routing functions.
def router(app):
    """
    Routing functions.

    Parameters
    ----------
    app : flask application
        App to define routes for.
    """

    # Index route.
    @app.route('/')
    @app.route('/index')
    def index():
        """
        Index Router Function.

        Returns
        -------
        str
            HTML content to be displayed.
        """
        return render_template('index.html', title='Home')
    return
