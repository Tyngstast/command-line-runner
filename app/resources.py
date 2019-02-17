from flask_restful import Resource, abort
import subprocess

class Commands(Resource):
    def get(self):
        result = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE)
        if (result.returncode != 0):
            return abort(500)

        return result.stdout.decode("UTF-8")
