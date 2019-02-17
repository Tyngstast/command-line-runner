import os
# import sys

# PACKAGE_PARENT = '..'
# SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
# sys.path.append(os.path.join(SCRIPT_DIR, PACKAGE_PARENT))

from app import db
from config import DB_FILE

if not os.path.isfile(DB_FILE):
    print('Creating database...')
    db.create_all()
    print('Database created')