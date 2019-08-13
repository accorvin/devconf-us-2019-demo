from .. import metrics

from api.main import bp
from flask import jsonify


# Define a route and the endpoint that it's availalbe at
# Multiple url endpoints are allowed.
@bp.route('/')
@bp.route('/index')
def index():
    metrics.SITE_ACCESSED_COUNTER.inc()
    return jsonify(response='Hello, World!')
