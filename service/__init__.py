import os
from flask import Flask, request, jsonify

from service.views import views
from service
from pymongo import MongoClient


app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

client = MongoClient(os.environ.get("MONGODB_URL"))
db = client["ml_service"]


@app.route('/')
def index():
    return jsonify(
        status=True,
        message='Welcome to the Dockerized Flask MongoDB app!'
    )


@app.route('/todo')
def todo():
    _todos = db.todo.find()

    item = {}
    data = []
    for todo in _todos:
        item = {
            'id': str(todo['_id']),
            'todo': todo['todo']
        }
        data.append(item)

    return jsonify(
        status=True,
        data=data
    )


@app.route('/todo', methods=['POST'])
def createTodo():
    data = request.get_json(force=True)
    item = {
        'todo': data['todo']
    }
    db.todo.insert_one(item)

    return jsonify(
        status=True,
        message='To-do saved successfully!'
    ), 201