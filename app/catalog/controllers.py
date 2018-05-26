# Import flask dependencies
from flask import Blueprint, url_for,abort,json,jsonify

# Import the database object from the main app module
from app import db

# Define the blueprint: 'catalog', set its url prefix: app.url/catalog
# This is used to define Component Prefix for routes
catalog_module = Blueprint('catalog', __name__, url_prefix='/catalog')

# Defining  routes and accepted methods, you can also add GET and POST together

@catalog_module.route('/productScore/', methods=['GET'])

def productScore():
    try:
        return jsonify({
            "Hello":"World"
        })
    except:
        abort(402)