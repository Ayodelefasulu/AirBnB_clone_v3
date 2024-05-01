#!/usr/bin/python3
""" Blueprint for flask  """

from flask import Blueprint
from api.v1.views.index import *
from api.v1.views.index import app_views
from api.v1.views import states
from api.v1.views import cities
from api.v1.views import amenities
from api.v1.views import users
from api.v1.views import places
from api.v1.views import places_reviews

# Create Blueprint
def create_app(app):
    """Register blueprint"""
    app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
