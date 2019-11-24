"""
This package is a flask application that presently does nothing.
"""
# Imports
import os

from flask import Flask

from testapp import auth
from testapp import database
from testapp.config import Config
from testapp.router import router


# App factory function.
def create_app():
    """Flask app factory function.
    """
    # Create Flask app from testapp package.
    app = Flask(__name__, instance_relative_config=True)

    # Import configuration object.
    app.config.from_object(Config)

    # Ensure application directories exist.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Create and allow access to routing functions.
    router(app)

    # Create and/or access database.
    database.initapp(app)

    # Register authentication blueprint
    app.register_blueprint(auth.bp)

    # Return the fully functional application.
    return app
