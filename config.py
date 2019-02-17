import os

basedir = os.path.abspath(os.path.dirname(__file__))
DB_FILE = 'app.db'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, DB_FILE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
