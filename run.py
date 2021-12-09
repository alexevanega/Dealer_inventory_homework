from cd_app import app
from cd_app.models import db, User

@app.shell_context_processor
def shell_context():
    return {'db': db, 'User': User }

