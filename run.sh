#!/bin/sh

# Run gunicorn, a production-ready Flask server.
# Listen on all interfaces at port 5000
# Direct the access and error logs to standard out
# Tell gunicorn that the Flask app can be found in the app.py module as
#   the app object.
exec gunicorn -b 0.0.0.0:5000 --access-logfile - --error-logfile - app:app
