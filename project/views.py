from flask import Blueprint, jsonify, make_response, request

from project.calculations import options
from project.models import LaunchModel
from project.serializers import RequestSerializer

OPTIONS = {
    "segmentation": options.segmentation,
}

views = Blueprint("views", __name__)


@views.route("/start_launch", methods=["POST"])
def results():
    if request.method == "POST":
        try:
            request_data = RequestSerializer(**request.form)
        except ValueError as err:
            error = f"Bad request! Error - {err}"
            return make_response(jsonify(error=error), 404)

        try:
            variant = OPTIONS[request_data.option]
        except KeyError as error:
            error = f"Key {error} doesn't exists!"
            return make_response(jsonify(error=error), 404)

        result = variant(request_data)

        return make_response(jsonify(result), 200)


@views.route("/history", methods=["GET"])
def records():
    all_launches = LaunchModel.query.order_by(LaunchModel.id)
    data = [
        {
            "id": launch.id,
            "model": launch.model,
            "date": launch.date,
            "image_name": launch.image_name,
            "image_height": launch.image_height,
            "image_width": launch.image_width,
            "success": launch.success,
        }
        for launch in all_launches.all()
    ]
    return make_response(data, 200)
