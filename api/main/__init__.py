from flask import Blueprint

# Create the route blueprint to handle API routing
bp = Blueprint('main', __name__)

# Import all of the routes in the main module
# Also ignore python linting rules for this import being
# unused and not appearing at the top of the module. This import is
# located here at the bottom to avoid a circular dependency issue.
from api.main import routes  # noqa: E402,F401
