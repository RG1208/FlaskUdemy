from flask import Flask # type: ignore
from config import Config
from models import db  # type: ignore

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
