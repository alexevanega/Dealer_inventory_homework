from flask import Blueprint, render_template, request
from wtforms.fields.simple import PasswordField
from flask import redirect, url_for

from cd_app.routes import homePage

from .forms import userForm
from ..models import User

from cd_app import db

auth = Blueprint('authenticate',__name__,template_folder='auth_templates')


@auth.route('/login')
def logIn():
    return render_template('log_in.html')

@auth.route('/signup', methods=["POST","GET"])
def signUp():
    auth_form = userForm()
    if request.method == 'POST':
        if auth_form.validate():
            first = auth_form.first_name.data
            last = auth_form.last_name.data
            email = auth_form.email.data
            password = auth_form.password.data

            user = User(first,last,email,password)

            db.session.add(user)
            db.session.commit()
            
            return redirect({{ url_for(homePage) }})
            
    return render_template('sign_up.html', form=auth_form)