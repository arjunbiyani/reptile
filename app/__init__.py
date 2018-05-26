# Import flask and template operators
from flask import Flask, render_template
from flaskext.mysql import MySQL
import os
# Application Definition
app = Flask(__name__)
mysql = MySQL()
# Configurations
app.config.from_object(os.getenv('environment'))
# for using .env file pip install python-dotenv
# Define the database object which is imported
# by modules and controllers

db = mysql.init_app(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('error/404.html'), 404

# Import a module / component using its blueprint handler variable (catalog_module)
from app.catalog.controllers import catalog_module

# Register blueprint(s)
app.register_blueprint(catalog_module)
# app.register_blueprint({module name}})
    