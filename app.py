from os import name
from flask import Flask, request, jsonify

app = Flask(__name__)

stores = [
    {
        "name": "My Wonderful Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]

@app.get("/store")
def get_stores():
    return {"stores": stores}

@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return {"message": "Store created successfully", "store": new_store}, 201

@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    item = {
        "name": request_data["name"],
        "price": request_data["price"]
    }
    
    for store in stores:
        if store["name"] == name:
            store["items"].append(item)
            return {"message": "Item added successfully", "item": item}, 201
    
    return {"message": "Store not found"}, 404

@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return {"store": store}
    return {"message": "Store not found"}, 404

@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"],"message": "Items retrieved successfully"}
    return {"message": "Store not found"}, 404