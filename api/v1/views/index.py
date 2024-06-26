#!/usr/bin/python3
""" Index page of the app """

from flask import Flask, jsonify, Blueprint
from models import storage
from api.v1.views import app_views
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


# app_views = Blueprint('app_views', __name__)

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """Endpoint to check the status of the API.

    Returns:
        JSON response containing the status.
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """Retrieve the number of each object type.

    Returns:
        JSON response containing the counts of different object types.
    """
    print("This is not working")
    stats = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }
    return jsonify(stats)
