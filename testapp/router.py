"""
This file contains router functions for flask to access from test.py.

Functions
---------
    index
        This is the route for '/' and '/index'
"""
from flask import current_app


def router(app):
    """
    Router function subroutines

    Parameters
    ----------
    app : flask application
        App to define routes for
    """
    @current_app.route('/')
    @current_app.route('/index')
    def index():
        """
        Index Router Function.

        Returns
        -------
        str
            HTML content to be displayed.
        """
        return "<h1>Hello World!</h1>"
    return
