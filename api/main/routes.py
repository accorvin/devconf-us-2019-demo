import random
import socket
import string


from .. import metrics
from api.main import bp
from flask import jsonify
from flask_api import status


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


@bp.route('/random')
def random_route():
    STRING_LENGTH = 300000000

    long_str = ''.join(random.choice(string.ascii_uppercase) for i in range(1)) * \
        STRING_LENGTH
    return jsonify(message='Random load generated')
