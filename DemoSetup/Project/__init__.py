from flask import Flask,Blueprint  # type: ignore
from .routes import main  # type: ignore
from .extensions import db  # type: ignore

def create_app():
    app = Flask(__name__)
    app.config.from_prefixedenv()
    db.init_app(app)
    app.register_blueprint(main)

    return app
