import socket

from .. import metrics
from .. import load
from api.main import bp
from flask import jsonify
from flask_api import status


MEMORY_HOG = None


# Define a route and the endpoint that it's availalbe at
# Multiple url endpoints are allowed.
@bp.route('/')
@bp.route('/index')
def index():
    hostname = socket.gethostname()
    metrics.SITE_ACCESSED_COUNTER.inc()
    return jsonify(response='Hello, World!',
                   hostname=hostname)


@bp.route('/error')
def error():
    metrics.SITE_ERROR_COUNTER.inc()
    return (jsonify(message='This page generated an error!'),
            status.HTTP_400_BAD_REQUEST)


@bp.route('/load')
def add_load():
    load.MEMORY_LOAD.append(bytearray(100000000))
    return jsonify(message='Load generated')
