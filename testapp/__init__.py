"""
This package is a flask application that presently does nothing.
"""
# Imports
from flask import Flask
from testapp.config import Config
from testapp.router import router


# App factory function
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    router(app)
    return app
