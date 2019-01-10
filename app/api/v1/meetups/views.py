"""views for Meetups"""
from flask import jsonify, request
from flask_restful import Resource

from .models import MeetupsModel


class Meetups(Resource):
    """docstring for Meetups class"""

    def __init__(self):
        """initiliase the Meetups class"""
        self.db = MeetupsModel()

    def post(self):
        """docstring for saving a Meetup"""
        meetup_id = self.db.save()

        return jsonify({
            "status": 201,
            "data": {
                "id": meetup_id,
                "topic": request.json.get('topic'),
                "location": request.json.get('location'),
                "happeningOn":request.json.get('happeningOn'),
                "tags":request.json.get('tags')
            }
        })

    def get(self):
        """docstring for fetching all the meetups posted"""
        self.db.get_all()
        return jsonify({
            "status": 200,
            "data": self.db.get_all()
        })