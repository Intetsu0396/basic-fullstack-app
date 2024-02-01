"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Item
from api.utils import generate_sitemap, APIException
from flask_cors import CORS


api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Mi primer proyecto fullStack, mira madrecita estoy triunfando !!!"
    }

    return jsonify(response_body), 200

@api.route("/items", methods=["GET"])
def get_items():

    response_items = Item.query.all()
    return jsonify({"items": [item.serialize() for item in response_items ]})

@api.route("/item", methods=["POST"])
def create_item():

    body= request.json
    name_body= body.get("name", None)
    price_body= body.get("price", None)

    if name_body is None or price_body is None:
        return jsonify({"error": "You need a Name and a Price"}), 400
    
    new_item = Item(name= name_body, price = price_body)
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"success": "Item created!!"})

