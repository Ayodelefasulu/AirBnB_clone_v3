#!/usr/bin/python3
"""State api endpoints"""
from api.v1.views import app_views
from flask import jsonify, request
from models import storage, State

@app_views.route('/states', methods=['GET'])
def get_all_states():
    """Retrieve a list of all State objects"""
    states = storage.all(State).values()
    states_list = [state.to_dict() for state in states]
    return jsonify(states_list)

@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """Retrieve a State object by ID"""
    state = storage.get(State, state_id)
    if state:
        return jsonify(state.to_dict())
    else:
        abort(404)

@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """Delete a State object by ID"""
    state = storage.get(State, state_id)
    if state:
        state.delete()
        storage.save()
        return jsonify({})
    else:
        abort(404)

@app_views.route('/states', methods=['POST'])
def create_state():
    """Create a new State object"""
    if not request.json:
        abort(400, 'Not a JSON')
    if 'name' not in request.json:
        abort(400, 'Missing name')
    state_data = request.json
    new_state = State(**state_data)
    new_state.save()
    return jsonify(new_state.to_dict()), 201

@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """Update a State object by ID"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not request.json:
        abort(400, 'Not a JSON')
    state_data = request.json
    # Update state attributes except 'id', 'created_at', 'updated_at'
    for key, value in state_data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict())
