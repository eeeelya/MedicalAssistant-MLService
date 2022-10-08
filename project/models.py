from project.extensions import db
from datetime import datetime


class LaunchModel(db.Model):
    __table_name__ = "launches"

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(128), unique=False, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now())
    image_height = db.Column(db.Integer, unique=False, nullable=False)
    image_width = db.Column(db.Integer, unique=False, nullable=False)
    image_name = db.Column(db.String(128), unique=False, nullable=False)
    success = db.Column(db.Boolean, unique=False, nullable=False)

    def __init__(self, model: str, image_height: int, image_width: int, success: bool, image_name: str, date):
        self.model = model
        self.date = date
        self.image_height = image_height
        self.image_width = image_width
        self.image_name = image_name
        self.success = success
