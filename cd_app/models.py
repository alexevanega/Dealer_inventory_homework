from cd_app import db
from enum import unique


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150),nullable=False)
    last_name = db.Column(db.String(150),nullable=False)
    email = db.Column(db.String(150),nullable=False, unique=True)
    password = db.Column(db.String(256),nullable=False)

    def __init__(self,first,last,email,password):
        self.first_name = first
        self.last_name = last
        self.email = email
        self.password = password
