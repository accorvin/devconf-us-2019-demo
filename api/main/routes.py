import socket
import random
import threading


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
    THREADS = 5
    ROUNDS = 1000000

    def f():
        for i in range(ROUNDS):
            random.randint(0, 999999)
        return

    for i in range(THREADS):
        t = threading.Thread(target=f)
        t.start()

    return jsonify(message='Load generated')
