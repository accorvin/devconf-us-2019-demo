import logging
import sys

from flask import Flask


# This create_app function creates the master Flask app object
def create_app():
    app = Flask(__name__)

    # Register the main API routes
    from api.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Enable logging for production
    if not app.debug and not app.testing:
        log = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(('%(asctime)s - %(name)s - '
                                       '%(levelname)s - %(message)s'))
        log.setFormatter(formatter)
        log.setLevel(logging.INFO)
        app.logger.addHandler(log)
        app.logger.setLevel(logging.INFO)

    return app
