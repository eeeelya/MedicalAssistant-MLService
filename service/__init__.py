from flask import Flask

from service.config import MONGODB_URI, MONGODB_DATABASE
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient(MONGODB_URI)
db = client[MONGODB_DATABASE]
