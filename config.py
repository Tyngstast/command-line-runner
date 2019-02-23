import os

basedir = os.path.abspath(os.path.dirname(__file__))
DB_FILE = os.path.join(basedir, 'app.db')

API_KEY = os.environ['CLR_API_KEY']

# DB file
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB_FILE
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Bundle reqparse errors 
BUNDLE_ERRORS = True
