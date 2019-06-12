# Import flask and template operators
from flask import Flask, render_template
from celery import Celery
import os
# Application Definition
app = Flask(__name__)

#Celery Configration
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery('reptile', broker=app.config['CELERY_BROKER_URL'])
#celery.conf.update(app.config)
@celery.task
def my_background_task(arg1, arg2):
    # some long running task here
    return "Executed Celery Task "

task = my_background_task.apply_async(args=[10, 20], countdown=10)
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
    