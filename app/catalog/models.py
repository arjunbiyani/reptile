# Import the database object (db) from the main application module
# We have define this inside /app/__init__.py in the next sections.
from app import db

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id          = db.Column(db.Integer, primary_key=True)
    order_id    = db.Column(db.Integer, unique=True)
    created_at  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

# Define a Orders model
class User(Base):

    __tablename__ = 'orders'

   # This model is not complete 

    # New instance instantiation procedure
    def __init__(self, order_id):

        self.order_id     = order_id