from flask import Flask
from app.routes.routes import ner_app

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    app.register_blueprint(ner_app, url_prefix='/')

    return app
