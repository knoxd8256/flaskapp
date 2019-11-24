"""
File containing configuration values for flask application testapp.
"""
# Import os and define the basedir variable as the root directory of the flaskGallery app
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Configuration for Flask application testapp

    Attributes
    ----------
        'SECRET_KEY'
            Secret key value for certain authorization/verification things.
        'UPLOAD_FOLDER'
            Folder to put file uploads into.
        'BASE_DIRECTORY'
            Flask application base directory.
        'DATABASE'
            Database to access and reference.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    BASE_DIRECTORY = basedir
    UPLOAD_FOLDER = os.path.join(basedir, 'picuploads'),
    DATABASE = os.path.join(basedir, 'flaskapp.sqlite')
