"""model for view for meetups"""
import datetime

from flask import jsonify,request
from flask_restful import Resource

meetups = []


class MeetupsModel():
    """Class with methods to perform CRUD operations on the DB"""

    def __init__(self):
        self.db = meetups
        if len(meetups) == 0:
            self.id = 1
        else:
            self.id = meetups[-1]['id'] + 1
        self.id = len(meetups) + 1

    def save(self):
        data = {
            'id': self.id,
            'createdOn': datetime.datetime.utcnow(),
            'createdBy': request.json.get('createdBy'),
            'title': request.json.get('title'),
            'question': request.json.get('question')
        }

        self.db.append(data)
        return self.id