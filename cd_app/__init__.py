from flask import Flask

from .inventory.routes import inv

app = Flask(__name__)

app.register_blueprint(inv)

from cd_app import routes