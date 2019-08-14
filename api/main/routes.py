from .. import metrics

from api.main import bp
from flask import jsonify
from flask_api import status


# Define a route and the endpoint that it's availalbe at
# Multiple url endpoints are allowed.
@bp.route('/')
@bp.route('/index')
def index():
    metrics.SITE_ACCESSED_COUNTER.inc()
    return jsonify(response='Hello, World!')


@bp.route('/error')
def error():
    metrics.SITE_ERROR_COUNTER.inc()
    return (jsonify(message='This page generated an error!'),
            status.HTTP_400_BAD_REQUEST)
