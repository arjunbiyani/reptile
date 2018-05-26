# Define the application directory
import os
class ProductionConfig(object):
    DEBUG = False
    TESTING = False
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

    # Define the database Config
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = 'licious'
    MYSQL_DATABASE_DB = 'licious'
    MYSQL_DATABASE_HOST = 'localhost'

    # Application threads.Just Like node JS Pm2 Clusters
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)
    CSRF_ENABLED     = True

    # Use a secure, unique and absolutely secret key for
    # signing the data. 
    CSRF_SESSION_KEY = "secret"

    # Secret key for signing cookies
    SECRET_KEY = "secret"

class DevelopmentConfig(ProductionConfig):
    DEBUG = True
    TESTING = True


class TestingConfig(ProductionConfig):
    DEBUG = False
    TESTING = True
