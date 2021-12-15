from datetime import datetime
from flask_login.mixins import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash


db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150),nullable=False)
    last_name = db.Column(db.String(150),nullable=False)
    email = db.Column(db.String(150),nullable=False, unique=True)
    password = db.Column(db.String(256),nullable=False)

    def __init__(self,first,last,email,password):
        self.first_name = first
        self.last_name = last
        self.email = email
        self.password = generate_password_hash(password)

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(300))
    vin_num = db.Column(db.String(16), nullable=False, unique=False)
    year = db.Column(db.String(4), nullable=True, unique=False)
    make = db.Column(db.String(25), nullable=True, unique=False)
    model = db.Column(db.String(75), nullable=False, unique=False)
    description = db.Column(db.String(300))
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow()) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, image, vin_num, year, make, model, description,user_id):
        self.image = image
        self.vin_num = vin_num
        self.year = year
        self.make = make
        self.model = model
        self.description = description
        self.user_id = user_id

class Reserve(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(300))
    vin_num = db.Column(db.String(16), nullable=False, unique=False)
    year = db.Column(db.String(4), nullable=True, unique=False)
    make = db.Column(db.String(25), nullable=True, unique=False)
    model = db.Column(db.String(75), nullable=False, unique=False)
    description = db.Column(db.String(300))

    def __init__(self, image, vin_num, year, make, model, description):
        self.image = image
        self.vin_num = vin_num
        self.year = year
        self.make = make
        self.model = model
        self.description = description
