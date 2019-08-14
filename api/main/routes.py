import queue
import random
import socket
import string
import threading
import time


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
    THREADS = 1
    STRING_LENGTH = 300000000

    def process_queue(q):
        while True:
            q.get()
            time.sleep(1)

    q = queue.Queue(maxsize=0)

    for i in range(THREADS):
        worker = threading.Thread(target=process_queue, args=(q,))
        worker.setDaemon(True)
        worker.start()

    str = ''.join(random.choice(string.ascii_uppercase) for i in range(1)) * \
        STRING_LENGTH
    q.put(str)
    q.join()
    return jsonify(message='Random load generated')
