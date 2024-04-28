#!/usr/bin/python3
""" Index page of the app """
from api.v1.views import app_views
from flask import jsonify

# Route /status
@app_views.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "OK"})
