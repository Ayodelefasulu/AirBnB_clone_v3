from flask import Blueprint
from api.v1.views.index import *

app_view = Blueprint('app_view', __name__, url_prefix='api/v1')