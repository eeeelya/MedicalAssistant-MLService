from flask import Flask

from project.views import views
from project.extensions import db


def create_app():
    app = Flask(__name__)
    app.config.from_object("project.config.Config")
    app.register_blueprint(views, url_prefix="/")

    db.init_app(app)

    return app

