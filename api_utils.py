import functools
import sys
import logging
from flask import request, jsonify

missing_msg = 'Missing parameter {}'
payload_mismatch = 'payload mismatch'

log = logging.getLogger()
log.addHandler(logging.StreamHandler(sys.stdout))
log.setLevel(logging.INFO)

def require_params(*params):
    def decorator(f):
        @functools.wraps(f)
        def wrap(*args, **kwargs):
            r = f(*args, **kwargs)
            for p in params:
                if p not in request.args or not request.args[p]:
                    return bad_request(missing_msg.format(p))
            return r
        return wrap
    return decorator

def require_payload_items(*params):
    def decorator(f):
        @functools.wraps(f)
        def wrap(*args, **kwargs):
            r = f(*args, **kwargs)
            data = request.get_json()
            for p in params:
                if p not in data or not data[p]:
                    return bad_request(payload_mismatch.format(p))
            return r
        return wrap
    return decorator

def bad_request(message):
    response = jsonify({'message': message})
    response.status_code = 400
    return response

def not_found():
    response = jsonify({'message': 'endpoint not found on this app.'})
    response.status_code = 404
    return response

def ok(message):
    response = jsonify({'message': message})
    response.status_code = 200
    return response

def internal_server_error():
  response = jsonify({'message': 'internal server error'})
  response.status_code = 500
  return response
