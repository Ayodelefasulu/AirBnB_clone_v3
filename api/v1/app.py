#!/usr/bin/python3
"""Main application script for running the API server.

This script creates Flask application, configures it with necessary settings,
including CORS for HTTP access control, blueprint registration,
error handling, and database connection management.

Attributes:
    app: A Flask instance representing the application.
"""

from flask import Flask, jsonify
from flask_cors import CORS
from api.v1.views import create_app
from models import storage
import os

# Create Flask app
app = Flask(__name__)

# Enable CORS (Cross-Origin Resource Sharing) for HTTP access control
cors = CORS(app, resources={r"/api/*": {"origins": "http://0.0.0.0:5000"}})

# Register the blueprint with the application
create_app(app)  # Call create_app function to register blueprints

def teardown_appcontext(exception):
    """Close the database connection when the app context ends.

    Args:
        exception: The exception, if any, occurred during app context teardown.
    """
    storage.close()


# Set up app context teardown handler
@app.teardown_appcontext
def teardown_appcontext(exception):
    """Close the database connection when the app context ends.

    Args:
        exception: The exception, if any, occurred during app context teardown.
    """
    storage.close()


# Define a custom error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors by returning a JSON-formatted response.

    Args:
        error: The 404 error that occurred.

    Returns:
        A JSON response containing an error message and status code 404.
    """
    return jsonify({"error": "Not found"}), 404


# Run the app if this file is executed directly
if __name__ == '__main__':
    # Get host and port from environment variables or use default values
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))

    # Run the Flask app
    app.run(host=host, port=port, threaded=True)
