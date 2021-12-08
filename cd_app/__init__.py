from flask import Flask
from config import Config

from .inventory.routes import inv

from .authenticate.routes import auth

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate(app,db)

app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(inv)
app.register_blueprint(auth)

from cd_app import routes
from cd_app import models