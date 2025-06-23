from flask import Blueprint   # type: ignore

main = Blueprint('main', __name__)

@main.route('/',methods=['GET', 'POST'])
def index():
    return "Hello, World!"
