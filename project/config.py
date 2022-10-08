import os

basedir = os.path.abspath(os.path.dirname(__file__))

AWS_KEY = os.environ.get("AWS_KEY")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")
AWS_REGION = os.environ.get("AWS_REGION")
RESULTS_BUCKET = os.environ.get("RESULTS_BUCKET")
SOURCES_BUCKET = os.environ.get("SOURCES_BUCKET")
MODELS_BUCKET = os.environ.get("MODELS_BUCKET")


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
