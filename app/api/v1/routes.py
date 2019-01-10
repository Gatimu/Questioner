"""all routes"""
from flask import Blueprint
from flask_restful import Api

from .meetups.views import Meetups

VERSION_ONE = Blueprint('api', __name__, url_prefix='/api/v1')
API = Api(VERSION_ONE)
API.add_resource(Meetups, '/meetups')
