from functools import wraps
from flask import request, abort
from config import API_KEY

def require_api_key(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if validate_api_key(request):
            return view_function(*args, **kwargs)
        else:
            abort(401)

    return decorated_function

def validate_api_key(request):
    auth_header = request.headers.get('Authorization')
    if auth_header:
        api_key = auth_header.split('API_KEY ')[1]
        if api_key == API_KEY:
            return True
    
    return False