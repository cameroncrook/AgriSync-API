# DESCRIPTION
# api routes for management (user creation, and farm management)

from flask import request, Blueprint, jsonify
import json

apiAgriSync = Blueprint('apiAgriSync', __name__, url_prefix='/api/v1')

@apiAgriSync.route('/test', methods=['GET'])
def test():
    testData = [
        {
            "name": "Fix fence by canal",
            "priority": "Urgent",
            "assigned_to": "Jayden",
            "status": 4,
            "id": 1
        },
        {
            "name": "Scatter grass seed in lower field",
            "priority": "Not Urgent",
            "assigned_to": "Anyone",
            "status": 3,
            "id": 2
        },
        {
            "name": "Tag new calf",
            "priority": "Urgent",
            "assigned_to": "Cameron",
            "status": 2,
            "id": 3
        }
    ]

    return jsonify(testData)

