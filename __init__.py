from flask import Flask
from flask_restful import Resource, Api
from .resources.commands import HelloWorld

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/')
