from flask import Blueprint  # type: ignore
from .models import MyModel  # type: ignore
main = Blueprint('main', __name__) # type: ignore

@main.route('/')
def index():
    return "Hello from the main blueprint!"