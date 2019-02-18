from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

import os
from app import models
from config import DB_FILE

if not os.path.isfile(DB_FILE):
    print('No database file, initializing...')
    db.create_all()

from flask_restful import Api
from app.rest.commands import CommandResource, CommandListResource
from app.rest.tags import TagResource, TagListResource

api = Api(app)
api.add_resource(CommandListResource, '/commands')
api.add_resource(CommandResource, '/commands/<id>')
api.add_resource(TagListResource, '/tags')
api.add_resource(TagResource, '/tags/<string:identifier>')