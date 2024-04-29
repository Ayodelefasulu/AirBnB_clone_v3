#!/usr/bin/python3
""" The main app """
from flask import Flask
from api.v1.views import app_views
from models import storage

# Create Flask app
app = Flask(__name__)

# Register blueprint
app.register_blueprint(app_views, url_prefix='/api/v1')

# Teardown app context to close database connection
@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()

# 404 error handler
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors by returning a JSON-formatted response"""
    return jsonify({"error": "Not found"}), 404


# Run the app if this file is executed directly
if __name__ == '__main__':
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
