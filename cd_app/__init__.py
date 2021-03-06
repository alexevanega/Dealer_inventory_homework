from flask import Flask
from config import Config

from .inventory.routes import inv
from .authenticate.routes import auth

from .models import db, User

from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

app.register_blueprint(inv)
app.register_blueprint(auth)

app.config.from_object(Config)

db.init_app(app)
login.init_app(app)

migrate = Migrate(app,db)

from cd_app import routes
from cd_app import models