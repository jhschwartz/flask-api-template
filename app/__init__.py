import os
from flask import Flask, request
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
import config

app = Flask(__name__)
akp_api = Api(app)
mongo = PyMongo(app)

from app import api