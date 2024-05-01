#!/usr/bin/python3
""" Users API endpoints  """
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.user import User

@app_views.route('/users', methods=['GET'])
def get_users():
    """Retrieve a list of all User objects"""
    users = [user.to_dict() for user in storage.all(User).values()]
    return jsonify(users)

@app_views.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """Retrieve a User object by ID"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())

@app_views.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a User object by ID"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    user.delete()
    storage.save()
    return jsonify({})

@app_views.route('/users', methods=['POST'])
def create_user():
    """Create a new User object"""
    if not request.json:
        abort(400, 'Not a JSON')
    if 'email' not in request.json:
        abort(400, 'Missing email')
    if 'password' not in request.json:
        abort(400, 'Missing password')
    user_data = request.json
    new_user = User(**user_data)
    new_user.save()
    return jsonify(new_user.to_dict()), 201

@app_views.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """Update a User object by ID"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    if not request.json:
        abort(400, 'Not a JSON')
    user_data = request.json
    # Update user attributes except 'id', 'email', 'created_at', 'updated_at'
    for key, value in user_data.items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict())
