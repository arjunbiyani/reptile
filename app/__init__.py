# Import flask and template operators
from flask import Flask, render_template
import os
# Application Definition
app = Flask(__name__)
# Configurations
app.config.from_object(os.getenv('environment'))
# for using .env file pip install python-dotenv
# Define the database object which is imported
# by modules and controllers


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('error/404.html'), 404

# Import a module / component using its blueprint handler variable (catalog_module)
from app.celery_test_app.controllers import celery_module

# Register blueprint(s)
app.register_blueprint(celery_module)
# app.register_blueprint({module name}})
    