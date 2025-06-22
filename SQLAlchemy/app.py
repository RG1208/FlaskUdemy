from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy # type: ignore

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db=SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    datejoined = db.Column(db.DateTime)

    orders = db.relationship('Order', back_populates='user')

order_product = db.Table("order_product",
        db.Column('order_id', db.Integer, db.ForeignKey('order.id'),primary_key=True),
        db.Column('product_id', db.Integer, db.ForeignKey('product.id'),primary_key=True)
    )

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String(80))
    user_id = db.Column(db.ForeignKey('user.id'))

    user= db.relationship('User', back_populates='orders')
    products = db.relationship('Product', secondary=order_product, back_populates='orders')

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float)
    orders = db.relationship('Order', secondary=order_product, back_populates='products')

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

def insertData():
    from datetime import datetime
    python_user = User(name="python_user", datejoined=datetime.now())
    javascript_user = User(name="javascript_user", datejoined=datetime.now())
    c_user = User(name="c_user", datejoined=datetime.now())

    db.session.add_all([python_user, javascript_user, c_user])

    firstOreder = Order(order_number="12345", user= python_user)
    secondOrder = Order(order_number="67890", user= javascript_user)
    thirdOrder = Order(order_number="86132", user= c_user)
    db.session.add_all([firstOreder, secondOrder,thirdOrder])
    db.session.commit()

def UpdateUser():
    user= User.query.first()
    user.name= "Rachit"
    db.session.commit()

def DeleteUser():
    user = User.query.first()
    db.session.delete(user)
    db.session.commit()

def queryTables():

    first_user = User.query.first()
    
    print("first user name:", first_user.name)
    for order in first_user.orders:
        print(f"Order Number: {order.order_number}, order ID: {order.id}")
    
    print("second user name")
    second_user = User.query.filter_by(id=2).first()
    for order in second_user.orders:
        print(f"Order Number: {order.order_number}, order ID: {order.id}")
    
def add_products_to_orders():
    first_product = Product(name="Laptop", price=1000.0)
    second_product = Product(name="Smartphone", price=500.0)
    third_product = Product(name="Tablet", price=300.0)

    db.session.add_all([first_product, second_product, third_product])

    first_order = Order.query.first()
    first_order.products.append(first_product)
    first_order.products.append(second_product) # Adding products to the first order

    db.session.commit()

def query_order_products():
    first_order = Order.query.first()
    second_order = Order.query.filter_by(id="2").first()

    print("first order products:")
    for product in first_order.products:
        print(f"Product Name: {product.name}, Price: {product.price}")
    
    print("second order products:")
    for product in second_order.products:
        print(f"Product Name: {product.name}, Price: {product.price}")

def get_all_users():
    users = User.query.all()

    for user in users:
        print(f"User ID: {user.id}, Name: {user.name}, Date Joined: {user.datejoined}")

    user_count = User.query.count()
    print(f"Total number of users: {user_count}")