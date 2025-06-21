from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy # type: ignore

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db=SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    datejoined = db.Column(db.DateTime)
@app.route('/')
def hello_world():
    return render_template("index.html",page_name="Home Page")

@app.route("/home", methods=["GET"])
def home():
    return "Welcome to the Home Page!"

@app.get("/json")
def json():
    return {"mykey": "JSON value", "myList": [1, 2, 3]}

@app.get("/dynamic", defaults={"user_input": "default_value"})
@app.get("/dynamic/<user_input>")
def dynamic(user_input):
    return f"The user entered: {user_input}"