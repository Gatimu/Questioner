"""Tests for meetups run with pytest"""
import json
import unittest

from ... import create_app

class MeetupsTestCase(unittest.TestCase):
    """This class represents the meetups test cases"""

    def setUp(self):
        APP = create_app("testing")
        self.app = APP.test_client()

        self.meetups = {
                "id" : 1,
                "location" : "Kisumu",
                "topic" :"Human Resource Meetup",
                "happeningOn" : "1/02/2019",
                "tags" : "HR"
            } 

    def test_post_redflag(self):
        response = self.app.post("/api/v1/meetups", headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.meetups))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)    
        