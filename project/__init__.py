from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from project.views import views


app = Flask(__name__)
app.config.from_object("project.config.Config")
app.register_blueprint(views, url_prefix="/")

db = SQLAlchemy(app)



