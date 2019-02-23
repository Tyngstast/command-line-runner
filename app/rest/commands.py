import os
import subprocess, shlex
from flask_restful import Resource, reqparse, abort
from app.models import *
from app import db

class CommandListResource(Resource):
    def get(self):
        commands = Command.query.all()
        if not commands:
            return abort(404, message="No commands in database")

        return commands_schema.dump(commands)
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('value', required=True, location='json')
        parser.add_argument('description', location='json')
        parser.add_argument('tags', type=list, location='json')
        args = parser.parse_args(strict=True)

        if Command.query.filter_by(value=args['value']).first():
            return abort(409)

        command = Command(args['value'], args['description'])

        for tag in args['tags'] or []:
            t = Tag.query.filter_by(value=tag).first()
            if t:
                command.tags.append(t)
            else:
                command.tags.append(Tag(tag))

        db.session.add(command)
        db.session.commit()

        return command_schema.dump(command), 201


class CommandResource(Resource):
    def get(self, id):
        command = Command.query.filter_by(id=id).first()

        if not command:
            return abort(404, message="Command not found")

        return command_schema.dump(command)
    
    def delete(self, id):
        command = Command.query.filter_by(id=id).first()

        if not command:
            return abort(404, message='Command not found')

        db.session.delete(command)
        db.session.commit()

        return '', 204


class CommandExecuteResource(Resource):
    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('args', action='append', location='args')
        query_params = parser.parse_args()
        print('params', query_params['args'])

        command = Command.query.filter_by(id=id).first()

        if not command:
            return abort(404, message='Command not found')

        popen_args = shlex.split(command.value)

        result = -1 
        try: 
            result = subprocess.run(popen_args, stdout=subprocess.PIPE)
        except FileNotFoundError:
            shell = os.environ['SHELL']
            shell = shell[shell.rfind('/')+1:]
            result = subprocess.run(['/bin/{}'.format(shell), '-c', '. {home}/.{shell}rc; {command} {params}'.format(
                home=os.environ['HOME'], 
                shell=shell,
                command=list_to_separated_string(popen_args),
                params=list_to_separated_string(query_params['args']))], 
                stdout=subprocess.PIPE)
        except Exception as e:
            return abort(500, message='Error executing command: {}'.format(str(e)))

        if (result.returncode != 0):
            print('error while executing', result)
            return abort(500, message='Error executing command. Code: {}'.format(result.returncode))

        return {'result': result.stdout.decode('UTF-8')}, 200

def list_to_separated_string(list, sep: str = ' '):
    if not list:
        return ''

    return sep.join(map(str, list))