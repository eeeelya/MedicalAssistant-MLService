from flask import Blueprint, jsonify

views = Blueprint("views", __name__)


@views.route("/")
def hello_world():
    return jsonify(hello="world")
