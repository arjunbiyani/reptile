# Import flask dependencies
from flask import Blueprint, url_for,abort,json,jsonify,request, current_app 


# Define the blueprint: 'test_module', set its url prefix: app.url/test
# This is used to define Component Prefix for routes

celery_module = Blueprint('celery', __name__, url_prefix='/celery')

# Defining  routes and accepted methods, you can also add GET and POST together

@celery_module.route('/', methods=['GET'])

def index():
    try:
        return "Celery Support"
    except Exception as e:
        return 
       
       